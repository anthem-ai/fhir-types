from typing import Any, List, Literal, TypedDict

from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing

# A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
FHIR_NutritionOrder_Administration = TypedDict(
    "FHIR_NutritionOrder_Administration",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The time period and frequency at which the enteral formula should be delivered to the patient.
        "schedule": FHIR_Timing,
        # The volume of formula to provide to the patient per the specified administration schedule.
        "quantity": FHIR_Quantity,
        # The rate of administration of formula via a feeding pump, e.g. 60 mL per hour, according to the specified schedule.
        "rateQuantity": FHIR_Quantity,
        # The rate of administration of formula via a feeding pump, e.g. 60 mL per hour, according to the specified schedule.
        "rateRatio": FHIR_Ratio,
    },
    total=False,
)
