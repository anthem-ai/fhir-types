from typing import Any, List, Literal, TypedDict

from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A container for a collection of resources.
FHIR_Bundle_Search = TypedDict(
    "FHIR_Bundle_Search",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.
        "mode": Literal["match", "include", "outcome"],
        # Extensions for mode
        "_mode": FHIR_Element,
        # When searching, the server's search ranking score for the entry.
        "score": FHIR_decimal,
        # Extensions for score
        "_score": FHIR_Element,
    },
    total=False,
)
