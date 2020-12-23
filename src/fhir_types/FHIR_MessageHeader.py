from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_MessageHeader_Destination import FHIR_MessageHeader_Destination
from .FHIR_MessageHeader_Response import FHIR_MessageHeader_Response
from .FHIR_MessageHeader_Source import FHIR_MessageHeader_Source
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
FHIR_MessageHeader = TypedDict(
    "FHIR_MessageHeader",
    {
        # This is a MessageHeader resource
        "resourceType": Literal["MessageHeader"],
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
        # Code that identifies the event this message represents and connects it with its definition. Events defined as part of the FHIR specification have the system value "http://terminology.hl7.org/CodeSystem/message-events".  Alternatively uri to the EventDefinition.
        "eventCoding": FHIR_Coding,
        # Code that identifies the event this message represents and connects it with its definition. Events defined as part of the FHIR specification have the system value "http://terminology.hl7.org/CodeSystem/message-events".  Alternatively uri to the EventDefinition.
        "eventUri": str,
        # Extensions for eventUri
        "_eventUri": FHIR_Element,
        # The destination application which the message is intended for.
        "destination": List[FHIR_MessageHeader_Destination],
        # Identifies the sending system to allow the use of a trust relationship.
        "sender": FHIR_Reference,
        # The person or device that performed the data entry leading to this message. When there is more than one candidate, pick the most proximal to the message. Can provide other enterers in extensions.
        "enterer": FHIR_Reference,
        # The logical author of the message - the person or device that decided the described event should happen. When there is more than one candidate, pick the most proximal to the MessageHeader. Can provide other authors in extensions.
        "author": FHIR_Reference,
        # The source application from which this message originated.
        "source": FHIR_MessageHeader_Source,
        # The person or organization that accepts overall responsibility for the contents of the message. The implication is that the message event happened under the policies of the responsible party.
        "responsible": FHIR_Reference,
        # Coded indication of the cause for the event - indicates  a reason for the occurrence of the event that is a focus of this message.
        "reason": FHIR_CodeableConcept,
        # Information about the message that this message is a response to.  Only present if this message is a response.
        "response": FHIR_MessageHeader_Response,
        # The actual data of the message - a reference to the root/focus class of the event.
        "focus": List[FHIR_Reference],
        # Permanent link to the MessageDefinition for this message.
        "definition": FHIR_canonical,
    },
    total=False,
)
