from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_CommunicationRequest_Payload import FHIR_CommunicationRequest_Payload
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
FHIR_CommunicationRequest = TypedDict(
    "FHIR_CommunicationRequest",
    {
        # This is a CommunicationRequest resource
        "resourceType": Literal["CommunicationRequest"],
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
        # Business identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # A plan or proposal that is fulfilled in whole or in part by this request.
        "basedOn": List[FHIR_Reference],
        # Completed or terminated request(s) whose function is taken by this new request.
        "replaces": List[FHIR_Reference],
        # A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar form.
        "groupIdentifier": FHIR_Identifier,
        # The status of the proposal or order.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Captures the reason for the current state of the CommunicationRequest.
        "statusReason": FHIR_CodeableConcept,
        # The type of message to be sent such as alert, notification, reminder, instruction, etc.
        "category": List[FHIR_CodeableConcept],
        # Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routine.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # If true indicates that the CommunicationRequest is asking for the specified action to *not* occur.
        "doNotPerform": FHIR_boolean,
        # Extensions for doNotPerform
        "_doNotPerform": FHIR_Element,
        # A channel that was used for this communication (e.g. email, fax).
        "medium": List[FHIR_CodeableConcept],
        # The patient or group that is the focus of this communication request.
        "subject": FHIR_Reference,
        # Other resources that pertain to this communication request and to which this communication request should be associated.
        "about": List[FHIR_Reference],
        # The Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # Text, attachment(s), or resource(s) to be communicated to the recipient.
        "payload": List[FHIR_CommunicationRequest_Payload],
        # The time when this communication is to occur.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # The time when this communication is to occur.
        "occurrencePeriod": FHIR_Period,
        # For draft requests, indicates the date of initial creation.  For requests with other statuses, indicates the date of activation.
        "authoredOn": FHIR_dateTime,
        # Extensions for authoredOn
        "_authoredOn": FHIR_Element,
        # The device, individual, or organization who initiated the request and has responsibility for its activation.
        "requester": FHIR_Reference,
        # The entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communication.
        "recipient": List[FHIR_Reference],
        # The entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communication.
        "sender": FHIR_Reference,
        # Describes why the request is being made in coded or textual form.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource whose existence justifies this request.
        "reasonReference": List[FHIR_Reference],
        # Comments made about the request by the requester, sender, recipient, subject or other participants.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
