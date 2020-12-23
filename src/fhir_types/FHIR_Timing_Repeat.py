from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_decimal import FHIR_decimal
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Range import FHIR_Range
from .FHIR_string import FHIR_string
from .FHIR_time import FHIR_time
from .FHIR_unsignedInt import FHIR_unsignedInt

# Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
FHIR_Timing_Repeat = TypedDict(
    "FHIR_Timing_Repeat",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.
        "boundsDuration": FHIR_Duration,
        # Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.
        "boundsRange": FHIR_Range,
        # Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.
        "boundsPeriod": FHIR_Period,
        # A total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count values.
        "count": FHIR_positiveInt,
        # Extensions for count
        "_count": FHIR_Element,
        # If present, indicates that the count is a range - so to perform the action between [count] and [countMax] times.
        "countMax": FHIR_positiveInt,
        # Extensions for countMax
        "_countMax": FHIR_Element,
        # How long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the duration.
        "duration": FHIR_decimal,
        # Extensions for duration
        "_duration": FHIR_Element,
        # If present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time length.
        "durationMax": FHIR_decimal,
        # Extensions for durationMax
        "_durationMax": FHIR_Element,
        # The units of time for the duration, in UCUM units.
        "durationUnit": Literal["s", "min", "h", "d", "wk", "mo", "a"],
        # Extensions for durationUnit
        "_durationUnit": FHIR_Element,
        # The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequency.
        "frequency": FHIR_positiveInt,
        # Extensions for frequency
        "_frequency": FHIR_Element,
        # If present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period range.
        "frequencyMax": FHIR_positiveInt,
        # Extensions for frequencyMax
        "_frequencyMax": FHIR_Element,
        # Indicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period length.
        "period": FHIR_decimal,
        # Extensions for period
        "_period": FHIR_Element,
        # If present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 days.
        "periodMax": FHIR_decimal,
        # Extensions for periodMax
        "_periodMax": FHIR_Element,
        # The units of time for the period in UCUM units.
        "periodUnit": Literal["s", "min", "h", "d", "wk", "mo", "a"],
        # Extensions for periodUnit
        "_periodUnit": FHIR_Element,
        # If one or more days of week is provided, then the action happens only on the specified day(s).
        "dayOfWeek": List[FHIR_code],
        # Extensions for dayOfWeek
        "_dayOfWeek": List[FHIR_Element],
        # Specified time of day for action to take place.
        "timeOfDay": List[FHIR_time],
        # Extensions for timeOfDay
        "_timeOfDay": List[FHIR_Element],
        # An approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occur.
        "when": List[
            Literal[
                "MORN",
                "MORN.early",
                "MORN.late",
                "NOON",
                "AFT",
                "AFT.early",
                "AFT.late",
                "EVE",
                "EVE.early",
                "EVE.late",
                "NIGHT",
                "PHS",
                "HS",
                "WAKE",
                "C",
                "CM",
                "CD",
                "CV",
                "AC",
                "ACM",
                "ACD",
                "ACV",
                "PC",
                "PCM",
                "PCD",
                "PCV",
            ]
        ],
        # Extensions for when
        "_when": List[FHIR_Element],
        # The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the event.
        "offset": FHIR_unsignedInt,
        # Extensions for offset
        "_offset": FHIR_Element,
    },
    total=False,
)
