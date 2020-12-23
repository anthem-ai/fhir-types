from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_time import FHIR_time

# The details of a healthcare service available at a location.
FHIR_HealthcareService_AvailableTime = TypedDict(
    "FHIR_HealthcareService_AvailableTime",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates which days of the week are available between the start and end Times.
        "daysOfWeek": List[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"]],
        # Extensions for daysOfWeek
        "_daysOfWeek": List[FHIR_Element],
        # Is this always available? (hence times are irrelevant) e.g. 24 hour service.
        "allDay": FHIR_boolean,
        # Extensions for allDay
        "_allDay": FHIR_Element,
        # The opening time of day. Note: If the AllDay flag is set, then this time is ignored.
        "availableStartTime": FHIR_time,
        # Extensions for availableStartTime
        "_availableStartTime": FHIR_Element,
        # The closing time of day. Note: If the AllDay flag is set, then this time is ignored.
        "availableEndTime": FHIR_time,
        # Extensions for availableEndTime
        "_availableEndTime": FHIR_Element,
    },
    total=False,
)
