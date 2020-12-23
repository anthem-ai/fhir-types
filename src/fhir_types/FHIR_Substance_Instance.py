from typing import Any, List, Literal, TypedDict

from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# A homogeneous material with a definite composition.
FHIR_Substance_Instance = TypedDict(
    "FHIR_Substance_Instance",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifier associated with the package/container (usually a label affixed directly).
        "identifier": FHIR_Identifier,
        # When the substance is no longer valid to use. For some substances, a single arbitrary date is used for expiry.
        "expiry": FHIR_dateTime,
        # Extensions for expiry
        "_expiry": FHIR_Element,
        # The amount of the substance.
        "quantity": FHIR_Quantity,
    },
    total=False,
)
