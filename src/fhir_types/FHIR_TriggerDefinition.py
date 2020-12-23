from typing import Any, List, Literal, TypedDict

from .FHIR_DataRequirement import FHIR_DataRequirement
from .FHIR_Element import FHIR_Element
from .FHIR_Expression import FHIR_Expression
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing

# A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
FHIR_TriggerDefinition = TypedDict(
    "FHIR_TriggerDefinition",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The type of triggering event.
        "type": Literal[
            "named-event",
            "periodic",
            "data-changed",
            "data-added",
            "data-modified",
            "data-removed",
            "data-accessed",
            "data-access-ended",
        ],
        # Extensions for type
        "_type": FHIR_Element,
        # A formal name for the event. This may be an absolute URI that identifies the event formally (e.g. from a trigger registry), or a simple relative URI that identifies the event in a local context.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # The timing of the event (if this is a periodic trigger).
        "timingTiming": FHIR_Timing,
        # The timing of the event (if this is a periodic trigger).
        "timingReference": FHIR_Reference,
        # The timing of the event (if this is a periodic trigger).
        "timingDate": str,
        # Extensions for timingDate
        "_timingDate": FHIR_Element,
        # The timing of the event (if this is a periodic trigger).
        "timingDateTime": str,
        # Extensions for timingDateTime
        "_timingDateTime": FHIR_Element,
        # The triggering data of the event (if this is a data trigger). If more than one data is requirement is specified, then all the data requirements must be true.
        "data": List[FHIR_DataRequirement],
        # A boolean-valued expression that is evaluated in the context of the container of the trigger definition and returns whether or not the trigger fires.
        "condition": FHIR_Expression,
    },
    total=False,
)
