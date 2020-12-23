from typing import Any, List, Literal, TypedDict

from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
FHIR_CodeableConcept = TypedDict(
    "FHIR_CodeableConcept",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # A reference to a code defined by a terminology system.
        "coding": List[FHIR_Coding],
        # A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
    },
    total=False,
)
