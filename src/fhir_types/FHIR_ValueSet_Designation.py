from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
FHIR_ValueSet_Designation = TypedDict(
    "FHIR_ValueSet_Designation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The language this designation is defined for.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A code that represents types of uses of designations.
        "use": FHIR_Coding,
        # The text value for this designation.
        "value": FHIR_string,
        # Extensions for value
        "_value": FHIR_Element,
    },
    total=False,
)
