from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Dosage_DoseAndRate import FHIR_Dosage_DoseAndRate
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing

# Indicates how the medication is/was taken or should be taken by the patient.
FHIR_Dosage = TypedDict(
    "FHIR_Dosage",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates the order in which the dosage instructions should be applied or interpreted.
        "sequence": FHIR_integer,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # Free text dosage instructions e.g. SIG.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # Supplemental instructions to the patient on how to take the medication  (e.g. "with meals" or"take half to one hour before food") or warnings for the patient about the medication (e.g. "may cause drowsiness" or "avoid exposure of skin to direct sunlight or sunlamps").
        "additionalInstruction": List[FHIR_CodeableConcept],
        # Instructions in terms that are understood by the patient or consumer.
        "patientInstruction": FHIR_string,
        # Extensions for patientInstruction
        "_patientInstruction": FHIR_Element,
        # When medication should be administered.
        "timing": FHIR_Timing,
        # Indicates whether the Medication is only taken when needed within a specific dosing schedule (Boolean option), or it indicates the precondition for taking the Medication (CodeableConcept).
        "asNeededBoolean": bool,
        # Extensions for asNeededBoolean
        "_asNeededBoolean": FHIR_Element,
        # Indicates whether the Medication is only taken when needed within a specific dosing schedule (Boolean option), or it indicates the precondition for taking the Medication (CodeableConcept).
        "asNeededCodeableConcept": FHIR_CodeableConcept,
        # Body site to administer to.
        "site": FHIR_CodeableConcept,
        # How drug should enter body.
        "route": FHIR_CodeableConcept,
        # Technique for administering medication.
        "method": FHIR_CodeableConcept,
        # The amount of medication administered.
        "doseAndRate": List[FHIR_Dosage_DoseAndRate],
        # Upper limit on medication per unit of time.
        "maxDosePerPeriod": FHIR_Ratio,
        # Upper limit on medication per administration.
        "maxDosePerAdministration": FHIR_Quantity,
        # Upper limit on medication per lifetime of the patient.
        "maxDosePerLifetime": FHIR_Quantity,
    },
    total=False,
)
