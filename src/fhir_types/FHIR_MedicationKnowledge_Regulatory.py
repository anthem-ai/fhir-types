from typing import Any, List, Literal, TypedDict

from .FHIR_MedicationKnowledge_MaxDispense import FHIR_MedicationKnowledge_MaxDispense
from .FHIR_MedicationKnowledge_Schedule import FHIR_MedicationKnowledge_Schedule
from .FHIR_MedicationKnowledge_Substitution import FHIR_MedicationKnowledge_Substitution
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Information about a medication that is used to support knowledge.
FHIR_MedicationKnowledge_Regulatory = TypedDict(
    "FHIR_MedicationKnowledge_Regulatory",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The authority that is specifying the regulations.
        "regulatoryAuthority": FHIR_Reference,
        # Specifies if changes are allowed when dispensing a medication from a regulatory perspective.
        "substitution": List[FHIR_MedicationKnowledge_Substitution],
        # Specifies the schedule of a medication in jurisdiction.
        "schedule": List[FHIR_MedicationKnowledge_Schedule],
        # The maximum number of units of the medication that can be dispensed in a period.
        "maxDispense": FHIR_MedicationKnowledge_MaxDispense,
    },
    total=False,
)
