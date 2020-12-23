from typing import Any, List, Literal, TypedDict

from .FHIR_Duration import FHIR_Duration
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# Information about a medication that is used to support knowledge.
FHIR_MedicationKnowledge_Kinetics = TypedDict(
    "FHIR_MedicationKnowledge_Kinetics",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The drug concentration measured at certain discrete points in time.
        "areaUnderCurve": List[FHIR_Quantity],
        # The median lethal dose of a drug.
        "lethalDose50": List[FHIR_Quantity],
        # The time required for any specified property (e.g., the concentration of a substance in the body) to decrease by half.
        "halfLifePeriod": FHIR_Duration,
    },
    total=False,
)
