from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_string import FHIR_string

# Indicates how the medication is/was taken or should be taken by the patient.
FHIR_Dosage_DoseAndRate = TypedDict(
    "FHIR_Dosage_DoseAndRate",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The kind of dose or rate specified, for example, ordered or calculated.
        "type": FHIR_CodeableConcept,
        # Amount of medication per dose.
        "doseRange": FHIR_Range,
        # Amount of medication per dose.
        "doseQuantity": FHIR_Quantity,
        # Amount of medication per unit of time.
        "rateRatio": FHIR_Ratio,
        # Amount of medication per unit of time.
        "rateRange": FHIR_Range,
        # Amount of medication per unit of time.
        "rateQuantity": FHIR_Quantity,
    },
    total=False,
)
