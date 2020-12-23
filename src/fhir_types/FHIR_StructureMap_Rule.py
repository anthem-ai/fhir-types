from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string
from .FHIR_StructureMap_Dependent import FHIR_StructureMap_Dependent
from .FHIR_StructureMap_Source import FHIR_StructureMap_Source
from .FHIR_StructureMap_Target import FHIR_StructureMap_Target

# A Map of relationships between 2 structures that can be used to transform data.
FHIR_StructureMap_Rule = TypedDict(
    "FHIR_StructureMap_Rule",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Name of the rule for internal references.
        "name": FHIR_id,
        # Extensions for name
        "_name": FHIR_Element,
        # Source inputs to the mapping.
        "source": List[FHIR_StructureMap_Source],
        # Content to create because of this mapping rule.
        "target": List[FHIR_StructureMap_Target],
        # Rules contained in this rule.
        "rule": List[Any],
        # Which other rules to apply in the context of this rule.
        "dependent": List[FHIR_StructureMap_Dependent],
        # Documentation for this instance of data.
        "documentation": FHIR_string,
        # Extensions for documentation
        "_documentation": FHIR_Element,
    },
    total=False,
)
