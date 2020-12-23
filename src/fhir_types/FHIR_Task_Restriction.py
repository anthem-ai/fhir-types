from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A task to be performed.
FHIR_Task_Restriction = TypedDict(
    "FHIR_Task_Restriction",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates the number of times the requested action should occur.
        "repetitions": FHIR_positiveInt,
        # Extensions for repetitions
        "_repetitions": FHIR_Element,
        # Over what time-period is fulfillment sought.
        "period": FHIR_Period,
        # For requests that are targeted to more than on potential recipient/target, for whom is fulfillment sought?
        "recipient": List[FHIR_Reference],
    },
    total=False,
)
