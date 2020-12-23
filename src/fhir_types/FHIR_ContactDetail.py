from typing import Any, List, Literal, TypedDict

from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# Specifies contact information for a person or organization.
FHIR_ContactDetail = TypedDict(
    "FHIR_ContactDetail",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The name of an individual to contact.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # The contact details for the individual (if a name was provided) or the organization.
        "telecom": List[FHIR_ContactPoint],
    },
    total=False,
)
