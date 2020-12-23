from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string

# Captures constraints on each element within the resource, profile, or extension.
FHIR_ElementDefinition_Mapping = TypedDict(
    "FHIR_ElementDefinition_Mapping",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An internal reference to the definition of a mapping.
        "identity": FHIR_id,
        # Extensions for identity
        "_identity": FHIR_Element,
        # Identifies the computable language in which mapping.map is expressed.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # Expresses what part of the target specification corresponds to this element.
        "map": FHIR_string,
        # Extensions for map
        "_map": FHIR_Element,
        # Comments that provide information about the mapping or its use.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
    },
    total=False,
)
