from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_time import FHIR_time

# Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
FHIR_Location_HoursOfOperation = TypedDict(
    "FHIR_Location_HoursOfOperation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates which days of the week are available between the start and end Times.
        "daysOfWeek": List[FHIR_code],
        # Extensions for daysOfWeek
        "_daysOfWeek": List[FHIR_Element],
        # The Location is open all day.
        "allDay": FHIR_boolean,
        # Extensions for allDay
        "_allDay": FHIR_Element,
        # Time that the Location opens.
        "openingTime": FHIR_time,
        # Extensions for openingTime
        "_openingTime": FHIR_Element,
        # Time that the Location closes.
        "closingTime": FHIR_time,
        # Extensions for closingTime
        "_closingTime": FHIR_Element,
    },
    total=False,
)
