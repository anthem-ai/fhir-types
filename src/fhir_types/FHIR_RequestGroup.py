from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_RequestGroup_Action import FHIR_RequestGroup_Action
from .FHIR_uri import FHIR_uri

# A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
FHIR_RequestGroup = TypedDict(
    "FHIR_RequestGroup",
    {
        # This is a RequestGroup resource
        "resourceType": Literal["RequestGroup"],
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
        # Allows a service to provide a unique, business identifier for the request.
        "identifier": List[FHIR_Identifier],
        # A canonical URL referencing a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this request.
        "instantiatesCanonical": List[FHIR_canonical],
        # Extensions for instantiatesCanonical
        "_instantiatesCanonical": List[FHIR_Element],
        # A URL referencing an externally defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this request.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # A plan, proposal or order that is fulfilled in whole or in part by this request.
        "basedOn": List[FHIR_Reference],
        # Completed or terminated request(s) whose function is taken by this new request.
        "replaces": List[FHIR_Reference],
        # A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar form.
        "groupIdentifier": FHIR_Identifier,
        # The current state of the request. For request groups, the status reflects the status of all the requests in the group.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Indicates the level of authority/intentionality associated with the request and where the request fits into the workflow chain.
        "intent": FHIR_code,
        # Extensions for intent
        "_intent": FHIR_Element,
        # Indicates how quickly the request should be addressed with respect to other requests.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # A code that identifies what the overall request group is.
        "code": FHIR_CodeableConcept,
        # The subject for which the request group was created.
        "subject": FHIR_Reference,
        # Describes the context of the request group, if any.
        "encounter": FHIR_Reference,
        # Indicates when the request group was created.
        "authoredOn": FHIR_dateTime,
        # Extensions for authoredOn
        "_authoredOn": FHIR_Element,
        # Provides a reference to the author of the request group.
        "author": FHIR_Reference,
        # Describes the reason for the request group in coded or textual form.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource whose existence justifies this request group.
        "reasonReference": List[FHIR_Reference],
        # Provides a mechanism to communicate additional information about the response.
        "note": List[FHIR_Annotation],
        # The actions, if any, produced by the evaluation of the artifact.
        "action": List[FHIR_RequestGroup_Action],
    },
    total=False,
)
