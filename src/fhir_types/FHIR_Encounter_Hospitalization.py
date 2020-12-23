from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
FHIR_Encounter_Hospitalization = TypedDict(
    "FHIR_Encounter_Hospitalization",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Pre-admission identifier.
        "preAdmissionIdentifier": FHIR_Identifier,
        # The location/organization from which the patient came before admission.
        "origin": FHIR_Reference,
        # From where patient was admitted (physician referral, transfer).
        "admitSource": FHIR_CodeableConcept,
        # Whether this hospitalization is a readmission and why if known.
        "reAdmission": FHIR_CodeableConcept,
        # Diet preferences reported by the patient.
        "dietPreference": List[FHIR_CodeableConcept],
        # Special courtesies (VIP, board member).
        "specialCourtesy": List[FHIR_CodeableConcept],
        # Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other things.
        "specialArrangement": List[FHIR_CodeableConcept],
        # Location/organization to which the patient is discharged.
        "destination": FHIR_Reference,
        # Category or kind of location after discharge.
        "dischargeDisposition": FHIR_CodeableConcept,
    },
    total=False,
)
