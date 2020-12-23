from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string
from .FHIR_StructureMap_Input import FHIR_StructureMap_Input
from .FHIR_StructureMap_Rule import FHIR_StructureMap_Rule

# A Map of relationships between 2 structures that can be used to transform data.
FHIR_StructureMap_Group = TypedDict(
    "FHIR_StructureMap_Group",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A unique name for the group for the convenience of human readers.
        "name": FHIR_id,
        # Extensions for name
        "_name": FHIR_Element,
        # Another group that this group adds rules to.
        "extends": FHIR_id,
        # Extensions for extends
        "_extends": FHIR_Element,
        # If this is the default rule set to apply for the source type or this combination of types.
        "typeMode": Literal["none", "types", "type-and-types"],
        # Extensions for typeMode
        "_typeMode": FHIR_Element,
        # Additional supporting documentation that explains the purpose of the group and the types of mappings within it.
        "documentation": FHIR_string,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # A name assigned to an instance of data. The instance must be provided when the mapping is invoked.
        "input": List[FHIR_StructureMap_Input],
        # Transform Rule from source to target.
        "rule": List[FHIR_StructureMap_Rule],
    },
    total=False,
)
