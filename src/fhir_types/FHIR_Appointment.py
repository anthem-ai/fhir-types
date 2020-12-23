from typing import Any, List, Literal, TypedDict

from .FHIR_Appointment_Participant import FHIR_Appointment_Participant
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_uri import FHIR_uri

# A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
FHIR_Appointment = TypedDict(
    "FHIR_Appointment",
    {
        # This is a Appointment resource
        "resourceType": Literal["Appointment"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # This records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation).
        "identifier": List[FHIR_Identifier],
        # The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status.
        "status": Literal[
            "proposed",
            "pending",
            "booked",
            "arrived",
            "fulfilled",
            "cancelled",
            "noshow",
            "entered-in-error",
            "checked-in",
            "waitlist",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The coded reason for the appointment being cancelled. This is often used in reporting/billing/futher processing to determine if further actions are required, or specific fees apply.
        "cancelationReason": FHIR_CodeableConcept,
        # A broad categorization of the service that is to be performed during this appointment.
        "serviceCategory": List[FHIR_CodeableConcept],
        # The specific service that is to be performed during this appointment.
        "serviceType": List[FHIR_CodeableConcept],
        # The specialty of a practitioner that would be required to perform the service requested in this appointment.
        "specialty": List[FHIR_CodeableConcept],
        # The style of appointment or patient that has been booked in the slot (not service type).
        "appointmentType": FHIR_CodeableConcept,
        # The coded reason that this appointment is being scheduled. This is more clinical than administrative.
        "reasonCode": List[FHIR_CodeableConcept],
        # Reason the appointment has been scheduled to take place, as specified using information from another resource. When the patient arrives and the encounter begins it may be used as the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a Procedure.
        "reasonReference": List[FHIR_Reference],
        # The priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority).
        "priority": FHIR_unsignedInt,
        # Extensions for priority
        "_priority": FHIR_Element,
        # The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment field.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Additional information to support the appointment provided when making the appointment.
        "supportingInformation": List[FHIR_Reference],
        # Date/Time that the appointment is to take place.
        "start": FHIR_instant,
        # Extensions for start
        "_start": FHIR_Element,
        # Date/Time that the appointment is to conclude.
        "end": FHIR_instant,
        # Extensions for end
        "_end": FHIR_Element,
        # Number of minutes that the appointment is to take. This can be less than the duration between the start and end times.  For example, where the actual time of appointment is only an estimate or if a 30 minute appointment is being requested, but any time would work.  Also, if there is, for example, a planned 15 minute break in the middle of a long appointment, the duration may be 15 minutes less than the difference between the start and end.
        "minutesDuration": FHIR_positiveInt,
        # Extensions for minutesDuration
        "_minutesDuration": FHIR_Element,
        # The slots from the participants' schedules that will be filled by the appointment.
        "slot": List[FHIR_Reference],
        # The date that this appointment was initially created. This could be different to the meta.lastModified value on the initial entry, as this could have been before the resource was created on the FHIR server, and should remain unchanged over the lifespan of the appointment.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # Additional comments about the appointment.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
        # While Appointment.comment contains information for internal use, Appointment.patientInstructions is used to capture patient facing information about the Appointment (e.g. please bring your referral or fast from 8pm night before).
        "patientInstruction": FHIR_string,
        # Extensions for patientInstruction
        "_patientInstruction": FHIR_Element,
        # The service request this appointment is allocated to assess (e.g. incoming referral or procedure request).
        "basedOn": List[FHIR_Reference],
        # List of participants involved in the appointment.
        "participant": List[FHIR_Appointment_Participant],
        # A set of date ranges (potentially including times) that the appointment is preferred to be scheduled within.The duration (usually in minutes) could also be provided to indicate the length of the appointment to fill and populate the start/end times for the actual allocated time. However, in other situations the duration may be calculated by the scheduling system.
        "requestedPeriod": List[FHIR_Period],
    },
    total=False,
)
