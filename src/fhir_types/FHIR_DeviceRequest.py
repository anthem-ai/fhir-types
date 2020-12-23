from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_DeviceRequest_Parameter import FHIR_DeviceRequest_Parameter
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri

# Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
FHIR_DeviceRequest = TypedDict(
    "FHIR_DeviceRequest",
    {
        # This is a DeviceRequest resource
        "resourceType": Literal["DeviceRequest"],
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
        # Identifiers assigned to this order by the orderer or by the receiver.
        "identifier": List[FHIR_Identifier],
        # The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this DeviceRequest.
        "instantiatesCanonical": List[FHIR_canonical],
        # The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this DeviceRequest.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # Plan/proposal/order fulfilled by this request.
        "basedOn": List[FHIR_Reference],
        # The request takes the place of the referenced completed or terminated request(s).
        "priorRequest": List[FHIR_Reference],
        # Composite request this is part of.
        "groupIdentifier": FHIR_Identifier,
        # The status of the request.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Whether the request is a proposal, plan, an original order or a reflex order.
        "intent": FHIR_code,
        # Extensions for intent
        "_intent": FHIR_Element,
        # Indicates how quickly the {{title}} should be addressed with respect to other requests.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # The details of the device to be used.
        "codeReference": FHIR_Reference,
        # The details of the device to be used.
        "codeCodeableConcept": FHIR_CodeableConcept,
        # Specific parameters for the ordered item.  For example, the prism value for lenses.
        "parameter": List[FHIR_DeviceRequest_Parameter],
        # The patient who will use the device.
        "subject": FHIR_Reference,
        # An encounter that provides additional context in which this request is made.
        "encounter": FHIR_Reference,
        # The timing schedule for the use of the device. The Schedule data type allows many different expressions, for example. "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # The timing schedule for the use of the device. The Schedule data type allows many different expressions, for example. "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".
        "occurrencePeriod": FHIR_Period,
        # The timing schedule for the use of the device. The Schedule data type allows many different expressions, for example. "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".
        "occurrenceTiming": FHIR_Timing,
        # When the request transitioned to being actionable.
        "authoredOn": FHIR_dateTime,
        # Extensions for authoredOn
        "_authoredOn": FHIR_Element,
        # The individual who initiated the request and has responsibility for its activation.
        "requester": FHIR_Reference,
        # Desired type of performer for doing the diagnostic testing.
        "performerType": FHIR_CodeableConcept,
        # The desired performer for doing the diagnostic testing.
        "performer": FHIR_Reference,
        # Reason or justification for the use of this device.
        "reasonCode": List[FHIR_CodeableConcept],
        # Reason or justification for the use of this device.
        "reasonReference": List[FHIR_Reference],
        # Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested service.
        "insurance": List[FHIR_Reference],
        # Additional clinical information about the patient that may influence the request fulfilment.  For example, this may include where on the subject's body the device will be used (i.e. the target site).
        "supportingInfo": List[FHIR_Reference],
        # Details about this request that were not represented at all or sufficiently in one of the attributes provided in a class. These may include for example a comment, an instruction, or a note associated with the statement.
        "note": List[FHIR_Annotation],
        # Key events in the history of the request.
        "relevantHistory": List[FHIR_Reference],
    },
    total=False,
)
