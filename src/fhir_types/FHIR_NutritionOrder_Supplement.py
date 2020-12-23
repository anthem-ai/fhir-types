from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing

# A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
FHIR_NutritionOrder_Supplement = TypedDict(
    "FHIR_NutritionOrder_Supplement",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The kind of nutritional supplement product required such as a high protein or pediatric clear liquid supplement.
        "type": FHIR_CodeableConcept,
        # The product or brand name of the nutritional supplement such as "Acme Protein Shake".
        "productName": FHIR_string,
        # Extensions for productName
        "_productName": FHIR_Element,
        # The time period and frequency at which the supplement(s) should be given.  The supplement should be given for the combination of all schedules if more than one schedule is present.
        "schedule": List[FHIR_Timing],
        # The amount of the nutritional supplement to be given.
        "quantity": FHIR_Quantity,
        # Free text or additional instructions or information pertaining to the oral supplement.
        "instruction": FHIR_string,
        # Extensions for instruction
        "_instruction": FHIR_Element,
    },
    total=False,
)
