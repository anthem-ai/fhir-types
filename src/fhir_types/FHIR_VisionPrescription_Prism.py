from typing import Any, List, Literal, TypedDict

from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# An authorization for the provision of glasses and/or contact lenses to a patient.
FHIR_VisionPrescription_Prism = TypedDict(
    "FHIR_VisionPrescription_Prism",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Amount of prism to compensate for eye alignment in fractional units.
        "amount": FHIR_decimal,
        # Extensions for amount
        "_amount": FHIR_Element,
        # The relative base, or reference lens edge, for the prism.
        "base": Literal["up", "down", "in", "out"],
        # Extensions for base
        "_base": FHIR_Element,
    },
    total=False,
)
