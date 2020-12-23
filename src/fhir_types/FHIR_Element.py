from typing import Any, List, Literal, TypedDict

from .FHIR_string import FHIR_string

# Base definition for all elements in a resource.
FHIR_Element = TypedDict(
    "FHIR_Element",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
    },
    total=False,
)
