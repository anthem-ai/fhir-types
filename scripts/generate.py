import json
import shutil
from pathlib import Path
from typing import Any, Dict, List, Set, Type, Union

Schema = Dict[str, Any]

# Definitions that lead to circular references
CIRCULAR_REFERENCES = {
    "Extension",
    "ResourceList",
    "QuestionnaireResponse_Answer",
    "GraphDefinition_Link",
    "ExampleScenario_Process",
    "ExampleScenario_Alternative",
}

# Definition.property that leads to circular references. Allows more fine grained
# control of override
CIRCULAR_PROPERTY_REFERENCES = {"Identifier": ["assigner"]}

# fhir.shema.json does not leverage "integer" type, so we hard code these special cases
INT_PROPERTIES = ["integer", "positiveInt", "unsignedInt"]


# Util functions
def get_resource_from_path(path: str) -> str:
    return path.split("/")[-1]


def get_resource_var_name(resource: str) -> str:
    return "FHIR_" + resource


def get_resource_file_name(resource: str) -> str:
    return "FHIR_" + resource


def get_import_line_from_reference(resource: str) -> str:
    file_name = get_resource_file_name(resource)
    var_name = get_resource_var_name(resource)
    return f"from .{file_name} import {var_name}\n"


# Parent class for definitions and properties
class SchemaDefinition:
    def __init__(self, name: str, schema: Schema):
        self.name = name
        self.schema = schema

    def get_description(self) -> str:
        return self.schema.get("description", "").replace("\n", "").replace("\r", "")

    def generate(self) -> str:  # pragma: nocover
        pass


# There are 3 definition types: OneOf, Primitive, Object
class OneOfDefinition(SchemaDefinition):
    def generate(self) -> str:
        file_output = "from typing import Union\n"

        # add imoprts
        for child_schema in self.schema["oneOf"]:
            resource = get_resource_from_path(child_schema["$ref"])
            file_output += get_import_line_from_reference(resource)

        file_output += f"{get_resource_var_name(self.name)} = Union[\n"

        # add Union Elements
        for child_schema in self.schema["oneOf"]:
            resource = get_resource_from_path(child_schema["$ref"])
            file_output += f"  {get_resource_var_name(resource)},\n"

        return file_output + "]"


class PrimitiveDefinition(SchemaDefinition):
    def generate(self) -> str:

        # default to string type for safety
        schema_type = self.schema.get("type", "string")

        if self.name in INT_PROPERTIES:
            result_type = "int"
        elif schema_type == "boolean":
            result_type = "bool"
        elif schema_type == "number":
            result_type = "float"
        elif schema_type == "string":
            result_type = "str"
        else:
            raise Exception("Not able to handle schema", self.schema)

        file_output = f"# {self.get_description()}\n"
        file_output += f"{get_resource_var_name(self.name)} = {result_type}"
        return file_output


class ObjectDefinition(SchemaDefinition):
    def generate(self) -> str:

        references: Set[str] = set()
        var_name = get_resource_var_name(self.name)

        end_file = f"# {self.get_description()}\n"
        end_file += f"{var_name} = TypedDict(\"{var_name}\", {'{'}\n"

        # Generate the end_file first so references can be collected
        for property_name in self.schema["properties"]:
            prop = Property(
                property_name, self.schema["properties"][property_name], self.name
            )

            prop_ref = prop.get_reference()
            if prop_ref and not prop.is_any_reference():
                references.add(prop_ref)

            end_file += prop.generate()

        end_file += "}, total=False)"

        # Generate imports from references
        start_file = "from typing import Any, List, TypedDict, Literal\n"

        for reference in references:
            start_file += get_import_line_from_reference(reference)

        return start_file + end_file


# Properties of ObjectDefinition schemas
class Property(SchemaDefinition):
    def __init__(self, name: str, schema: Schema, parent_resource: str):
        super().__init__(name, schema)
        self.parent_resource = parent_resource

    def _is_type(self, type_label) -> bool:
        return "type" in self.schema and self.schema["type"] == type_label

    def is_const(self) -> bool:
        return "const" in self.schema

    def is_enum(self) -> bool:
        return "enum" in self.schema

    def is_boolean(self) -> bool:
        return self._is_type("boolean")

    def is_number(self) -> bool:
        return self._is_type("number")

    def is_string(self) -> bool:
        return self._is_type("string")

    def is_array(self) -> bool:
        return self._is_type("array")

    def is_reference(self) -> bool:
        return "$ref" in self.schema

    def get_reference(self) -> Union[str, None]:
        if self.is_reference():
            return get_resource_from_path(self.schema["$ref"])
        elif self.is_array() and "$ref" in self.schema["items"]:
            return get_resource_from_path(self.schema["items"]["$ref"])
        return None

    # Helps deal with ciruclar reference mypy issues by using Any
    def is_any_reference(self) -> bool:
        ref_resource = self.get_reference()
        return ref_resource is not None and (
            ref_resource in CIRCULAR_REFERENCES
            or ref_resource == self.parent_resource
            or self.name in CIRCULAR_PROPERTY_REFERENCES.get(self.parent_resource, [])
        )

    def generate(self) -> str:
        line = f"  # {self.get_description()}\n"
        line += f'  "{self.name}": {self.generate_property()},\n'
        return line

    def generate_property(self) -> str:
        if self.is_const():
            return f"Literal[\"{self.schema['const']}\"]"
        elif self.is_enum():
            return Property.get_enum_literal(self.schema["enum"])
        elif self.is_boolean():
            return "bool"
        elif self.is_number():
            return "float"
        elif self.is_string():
            return "str"
        elif self.is_array():
            return self.generate_list_property(self.schema["items"])
        elif self.is_reference():
            return self.get_non_circular_reference(self.schema["$ref"])
        else:
            raise Exception("Property schema can not be handled:", self.schema)

    # Currently only $refs and enums are supported as lists
    def generate_list_property(self, items_schema) -> str:
        if len(items_schema.keys()) > 1:
            raise Exception("Expecting only one key in schema", items_schema)

        if "$ref" in items_schema:
            non_circular = self.get_non_circular_reference(items_schema["$ref"])
            return f"List[{non_circular}]"
        elif "enum" in items_schema:
            enums = Property.get_enum_literal(items_schema["enum"])
            return f"List[{enums}]"
        else:
            raise Exception(
                "array.items should have $ref or enum property", items_schema
            )

    def get_non_circular_reference(self, ref_path: str) -> str:
        if self.is_any_reference():
            return "Any"
        return get_resource_var_name(get_resource_from_path(ref_path))

    @staticmethod
    def get_enum_literal(enum):
        # Only support strings as enums now (All FHIR JSON enums are strings)
        strings = [f'"{string}"' for string in enum]
        return f"Literal[{', '.join(strings)}]"


def get_definition_class(
    definition_name: str, schema: Schema
) -> Type["SchemaDefinition"]:
    if "oneOf" in schema:
        return OneOfDefinition
    elif "properties" in schema:
        return ObjectDefinition
    elif definition_name[0].islower():
        return PrimitiveDefinition
    else:
        raise Exception("Not expecting this schema definition", definition_name, schema)


def get_init_py(definition_names: List[str]) -> str:
    """
    Returns the code needed for __init__.py, to allow for shorthand imports like
    `from fhir_types import FHIR_Bundle` instead of
    `from fhir_types.FHIR_Bundle import FHIR_Bundle`.
    """
    output = ""
    imports: List[str] = []
    for definition_name in definition_names:
        output += get_import_line_from_reference(definition_name)
        imports.append(get_resource_var_name(definition_name))
    output += f"__all__ = {repr(imports)}\n"
    return output


def get_schema() -> Schema:
    return json.loads(Path("fhir.schema.json").read_bytes())


def generate_files(schema: Schema, output_dir: Path) -> None:
    definition_names = []
    for definition_name, schema_def in schema["definitions"].items():
        definition_names.append(definition_name)
        resource_file_name = get_resource_file_name(definition_name)
        file_name = f"{resource_file_name}.py"

        klass = get_definition_class(definition_name, schema_def)
        definition = klass(definition_name, schema_def)
        output_dir.joinpath(file_name).write_text(definition.generate())

    output_dir.joinpath("__init__.py").write_text(get_init_py(definition_names))
    # Necessary for packaging:
    # https://mypy.readthedocs.io/en/latest/installed_packages.html
    output_dir.joinpath("py.typed").write_text("")


if __name__ == "__main__":

    output_dir = Path("src", "fhir_types")
    if output_dir.exists():
        # Clear directory first
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True)

    generate_files(get_schema(), output_dir)
