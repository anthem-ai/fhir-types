from typing import Any, List, Literal, TypedDict

from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# A set of ordered Quantities defined by a low and high limit.
FHIR_Range = TypedDict(
    "FHIR_Range",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The low limit. The boundary is inclusive.
        "low": FHIR_Quantity,
        # The high limit. The boundary is inclusive.
        "high": FHIR_Quantity,
    },
    total=False,
)
