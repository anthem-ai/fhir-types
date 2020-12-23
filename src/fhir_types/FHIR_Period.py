from typing import Any, List, Literal, TypedDict

from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A time period defined by a start and end date and optionally time.
FHIR_Period = TypedDict(
    "FHIR_Period",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The start of the period. The boundary is inclusive.
        "start": FHIR_dateTime,
        # Extensions for start
        "_start": FHIR_Element,
        # The end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that time.
        "end": FHIR_dateTime,
        # Extensions for end
        "_end": FHIR_Element,
    },
    total=False,
)
