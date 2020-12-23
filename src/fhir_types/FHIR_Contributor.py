from typing import Any, List, Literal, TypedDict

from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
FHIR_Contributor = TypedDict(
    "FHIR_Contributor",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The type of contributor.
        "type": Literal["author", "editor", "reviewer", "endorser"],
        # Extensions for type
        "_type": FHIR_Element,
        # The name of the individual or organization responsible for the contribution.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the contributor.
        "contact": List[FHIR_ContactDetail],
    },
    total=False,
)
