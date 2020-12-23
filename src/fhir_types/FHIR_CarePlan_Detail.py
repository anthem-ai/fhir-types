from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri

# Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
FHIR_CarePlan_Detail = TypedDict(
    "FHIR_CarePlan_Detail",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A description of the kind of resource the in-line definition of a care plan activity is representing.  The CarePlan.activity.detail is an in-line definition when a resource is not referenced using CarePlan.activity.reference.  For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
        "kind": FHIR_code,
        # Extensions for kind
        "_kind": FHIR_Element,
        # The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activity.
        "instantiatesCanonical": List[FHIR_canonical],
        # The URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activity.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # Detailed description of the type of planned activity; e.g. what lab test, what procedure, what kind of encounter.
        "code": FHIR_CodeableConcept,
        # Provides the rationale that drove the inclusion of this particular activity as part of the plan or the reason why the activity was prohibited.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource, such as the health condition(s), whose existence justifies this request and drove the inclusion of this particular activity as part of the plan.
        "reasonReference": List[FHIR_Reference],
        # Internal reference that identifies the goals that this activity is intended to contribute towards meeting.
        "goal": List[FHIR_Reference],
        # Identifies what progress is being made for the specific activity.
        "status": Literal[
            "not-started",
            "scheduled",
            "in-progress",
            "on-hold",
            "completed",
            "cancelled",
            "stopped",
            "unknown",
            "entered-in-error",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # Provides reason why the activity isn't yet started, is on hold, was cancelled, etc.
        "statusReason": FHIR_CodeableConcept,
        # If true, indicates that the described activity is one that must NOT be engaged in when following the plan.  If false, or missing, indicates that the described activity is one that should be engaged in when following the plan.
        "doNotPerform": FHIR_boolean,
        # Extensions for doNotPerform
        "_doNotPerform": FHIR_Element,
        # The period, timing or frequency upon which the described activity is to occur.
        "scheduledTiming": FHIR_Timing,
        # The period, timing or frequency upon which the described activity is to occur.
        "scheduledPeriod": FHIR_Period,
        # The period, timing or frequency upon which the described activity is to occur.
        "scheduledString": str,
        # Extensions for scheduledString
        "_scheduledString": FHIR_Element,
        # Identifies the facility where the activity will occur; e.g. home, hospital, specific clinic, etc.
        "location": FHIR_Reference,
        # Identifies who's expected to be involved in the activity.
        "performer": List[FHIR_Reference],
        # Identifies the food, drug or other product to be consumed or supplied in the activity.
        "productCodeableConcept": FHIR_CodeableConcept,
        # Identifies the food, drug or other product to be consumed or supplied in the activity.
        "productReference": FHIR_Reference,
        # Identifies the quantity expected to be consumed in a given day.
        "dailyAmount": FHIR_Quantity,
        # Identifies the quantity expected to be supplied, administered or consumed by the subject.
        "quantity": FHIR_Quantity,
        # This provides a textual description of constraints on the intended activity occurrence, including relation to other activities.  It may also include objectives, pre-conditions and end-conditions.  Finally, it may convey specifics about the activity such as body site, method, route, etc.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
    },
    total=False,
)
