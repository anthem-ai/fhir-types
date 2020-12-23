from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, List, Tuple

import pytest

from scripts.generate import (
    CIRCULAR_PROPERTY_REFERENCES,
    CIRCULAR_REFERENCES,
    INT_PROPERTIES,
    ObjectDefinition,
    OneOfDefinition,
    PrimitiveDefinition,
    Property,
    Schema,
    generate_files,
    get_definition_class,
    get_import_line_from_reference,
    get_init_py,
    get_resource_file_name,
    get_resource_from_path,
    get_resource_var_name,
    get_schema,
)


def test_utils() -> None:
    assert get_resource_from_path("#/definitions/Account") == "Account"
    assert get_resource_var_name("Account") == "FHIR_Account"
    assert get_resource_file_name("Account") == "FHIR_Account"
    import_line = "from .FHIR_Account import FHIR_Account\n"
    assert get_import_line_from_reference("Account") == import_line
    assert Property.get_enum_literal(["a", "b"]) == 'Literal["a", "b"]'


def test_get_definition() -> None:
    assert type(OneOfDefinition) == type(
        get_definition_class("Property", {"oneOf": []})
    )
    assert type(PrimitiveDefinition) == type(
        get_definition_class("boolean", {"properties": {}})
    )
    assert type(ObjectDefinition) == type(
        get_definition_class("Property", {"properties": {}})
    )

    with pytest.raises(Exception, match="Not expecting this schema definition"):
        get_definition_class("Property", {"oneOfQQQ": []})


def test_primitive_def() -> None:
    def build(line: str) -> str:
        return f"# aaa\n{line}"

    assert PrimitiveDefinition(
        "a", {"description": "aaa", "type": "string"}
    ).generate() == build("FHIR_a = str")

    assert PrimitiveDefinition(
        "a", {"description": "aaa", "type": "boolean"}
    ).generate() == build("FHIR_a = bool")

    assert PrimitiveDefinition(
        "a", {"description": "aaa", "type": "number"}
    ).generate() == build("FHIR_a = float")

    # No Type Provided (XHTML works this way)
    assert PrimitiveDefinition("a", {"description": "aaa"}).generate() == build(
        "FHIR_a = str"
    )

    # Check override INT
    prop_name = INT_PROPERTIES[0]
    assert PrimitiveDefinition(
        prop_name, {"description": "aaa", "type": "number"}
    ).generate() == build(f"FHIR_{prop_name} = int")

    # Check bad type given
    with pytest.raises(Exception, match="Not able to handle schema"):
        PrimitiveDefinition("a", {"description": "aaa", "type": "number123"}).generate()


def test_oneof_def() -> None:

    schema = {
        "oneOf": [{"$ref": "#/definitions/Account"}, {"$ref": "#/definitions/Patient"}]
    }

    lines = [
        "from typing import Union",
        "from .FHIR_Account import FHIR_Account",
        "from .FHIR_Patient import FHIR_Patient",
        "FHIR_Result = Union[",
        "  FHIR_Account,",
        "  FHIR_Patient,",
        "]",
    ]

    definition = OneOfDefinition("Result", schema)
    result = definition.generate().split("\n")

    for i in range(len(result)):
        assert result[i] == lines[i]


def test_object_def() -> None:
    schema = {
        "description": "aaa",
        "properties": {
            "a": {"description": "bbb", "type": "string"},
            "b": {"description": "bbb", "$ref": "#/definitions/Account"},
        },
    }

    lines = [
        "from typing import Any, List, TypedDict, Literal",
        "from .FHIR_Account import FHIR_Account",
        "# aaa",
        'FHIR_Result = TypedDict("FHIR_Result", {',
        "  # bbb",
        '  "a": str,',
        "  # bbb",
        '  "b": FHIR_Account,',
        "}, total=False)",
    ]

    definition = ObjectDefinition("Result", schema)
    result = definition.generate().split("\n")

    for i in range(len(result)):
        assert result[i] == lines[i]


def test_object_def_circular() -> None:
    circular_reference = list(CIRCULAR_REFERENCES)[0]
    circular_parent = list(CIRCULAR_PROPERTY_REFERENCES.keys())[0]
    circular_property = CIRCULAR_PROPERTY_REFERENCES[circular_parent][0]

    schema = {
        "description": "aaa",
        "properties": {
            # property can't point to self
            "a": {"description": "bbb", "$ref": f"#/definitions/{circular_parent}"},
            # circular references are blacklisted
            "b": {"description": "bbb", "$ref": f"#/definitions/{circular_reference}"},
            # reference.properties are blacklisted
            circular_property: {"description": "bbb", "$ref": "#/definitions/123"},
        },
    }

    # There should be no import references in any of these cases
    lines = [
        "from typing import Any, List, TypedDict, Literal",
        "# aaa",
        f"FHIR_{circular_parent} = TypedDict(\"FHIR_{circular_parent}\", {'{'}",
        "  # bbb",
        '  "a": Any,',
        "  # bbb",
        '  "b": Any,',
        "  # bbb",
        f'  "{circular_property}": Any,',
        "}, total=False)",
    ]

    definition = ObjectDefinition(circular_parent, schema)
    result = definition.generate().split("\n")

    for i in range(len(result)):
        assert result[i] == lines[i]


def test_property_gen() -> None:

    parent = "Parent"
    circular_reference = list(CIRCULAR_REFERENCES)[0]

    mappings: List[Tuple[str, Dict[str, Any]]] = [
        ("bool", {"description": "aaa", "type": "boolean"}),
        ("str", {"description": "aaa", "type": "string"}),
        ("float", {"description": "aaa", "type": "number"}),
        ('Literal["Account"]', {"description": "aaa", "const": "Account"}),
        ('Literal["a", "b"]', {"description": "aaa", "enum": ["a", "b"]}),
        ("FHIR_Account", {"description": "aaa", "$ref": "#/definitions/Account"}),
        (
            'List[Literal["a", "b"]]',
            {
                "description": "aaa",
                "type": "array",
                "items": {"enum": ["a", "b"]},
            },
        ),
        (
            "List[FHIR_Account]",
            {
                "description": "aaa",
                "type": "array",
                "items": {"$ref": "#/definitions/Account"},
            },
        ),
        # Circular Reference
        ("Any", {"description": "aaa", "$ref": f"#/definitions/{circular_reference}"}),
        # Self reference
        ("Any", {"description": "aaa", "$ref": f"#/definitions/{parent}"}),
    ]

    for result, schema in mappings:
        p = Property("prop_a", schema, parent)
        assert p.generate_property() == result

    # Check Circular Property as well
    circular_parent = list(CIRCULAR_PROPERTY_REFERENCES.keys())[0]
    circular_property = CIRCULAR_PROPERTY_REFERENCES[circular_parent][0]
    p2 = Property(
        circular_property,
        {"description": "aaa", "$ref": "#/definitions/123"},
        circular_parent,
    )
    assert p2.generate_property() == "Any"


def test_property_gen_fail() -> None:

    with pytest.raises(Exception, match="Property schema can not be handled"):
        schema: Schema = {"description": "aaa", "type": "123"}
        p = Property("prop_a", schema, "parent")
        p.generate()

    with pytest.raises(Exception, match=r"items should have \$ref or enum"):
        schema = {"description": "aaa", "type": "array", "items": {"type": "string"}}
        p = Property("prop_a", schema, "parent")
        p.generate()


def test_get_init_py() -> None:
    expected = """from .FHIR_foo import FHIR_foo
from .FHIR_bar import FHIR_bar
__all__ = ['FHIR_foo', 'FHIR_bar']
"""
    assert get_init_py(["foo", "bar"]) == expected


def test_generate_files_and_get_schema() -> None:
    with TemporaryDirectory() as _tempdir:
        tempdir = Path(_tempdir)
        generate_files(get_schema(), tempdir)
        assert tempdir.joinpath("__init__.py").exists()
        assert tempdir.joinpath("FHIR_Account.py").exists()
        assert tempdir.joinpath("FHIR_Patient.py").exists()
