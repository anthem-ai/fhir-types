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
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Task_Input import FHIR_Task_Input
from .FHIR_Task_Output import FHIR_Task_Output
from .FHIR_Task_Restriction import FHIR_Task_Restriction
from .FHIR_uri import FHIR_uri

# A task to be performed.
FHIR_Task = TypedDict(
    "FHIR_Task",
    {
        # This is a Task resource
        "resourceType": Literal["Task"],
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
        # The business identifier for this task.
        "identifier": List[FHIR_Identifier],
        # The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this Task.
        "instantiatesCanonical": FHIR_canonical,
        # The URL pointing to an *externally* maintained  protocol, guideline, orderset or other definition that is adhered to in whole or in part by this Task.
        "instantiatesUri": FHIR_uri,
        # Extensions for instantiatesUri
        "_instantiatesUri": FHIR_Element,
        # BasedOn refers to a higher-level authorization that triggered the creation of the task.  It references a "request" resource such as a ServiceRequest, MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the "request" resource the task is seeking to fulfill.  This latter resource is referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a task is created to fulfill a procedureRequest ( = FocusOn ) to collect a specimen from a patient.
        "basedOn": List[FHIR_Reference],
        # An identifier that links together multiple tasks and other requests that were created in the same context.
        "groupIdentifier": FHIR_Identifier,
        # Task that this particular task is part of.
        "partOf": List[FHIR_Reference],
        # The current status of the task.
        "status": Literal[
            "draft",
            "requested",
            "received",
            "accepted",
            "rejected",
            "ready",
            "cancelled",
            "in-progress",
            "on-hold",
            "failed",
            "completed",
            "entered-in-error",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # An explanation as to why this task is held, failed, was refused, etc.
        "statusReason": FHIR_CodeableConcept,
        # Contains business-specific nuances of the business state.
        "businessStatus": FHIR_CodeableConcept,
        # Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs this a proposed task, a planned task, an actionable task, etc.
        "intent": Literal[
            "unknown",
            "proposal",
            "plan",
            "order",
            "original-order",
            "reflex-order",
            "filler-order",
            "instance-order",
            "option",
        ],
        # Extensions for intent
        "_intent": FHIR_Element,
        # Indicates how quickly the Task should be addressed with respect to other requests.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # A name or code (or both) briefly describing what the task involves.
        "code": FHIR_CodeableConcept,
        # A free-text description of what is to be performed.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The request being actioned or the resource being manipulated by this task.
        "focus": FHIR_Reference,
        # The entity who benefits from the performance of the service specified in the task (e.g., the patient).
        "for": FHIR_Reference,
        # The healthcare event  (e.g. a patient and healthcare provider interaction) during which this task was created.
        "encounter": FHIR_Reference,
        # Identifies the time action was first taken against the task (start) and/or the time final action was taken against the task prior to marking it as completed (end).
        "executionPeriod": FHIR_Period,
        # The date and time this task was created.
        "authoredOn": FHIR_dateTime,
        # Extensions for authoredOn
        "_authoredOn": FHIR_Element,
        # The date and time of last modification to this task.
        "lastModified": FHIR_dateTime,
        # Extensions for lastModified
        "_lastModified": FHIR_Element,
        # The creator of the task.
        "requester": FHIR_Reference,
        # The kind of participant that should perform the task.
        "performerType": List[FHIR_CodeableConcept],
        # Individual organization or Device currently responsible for task execution.
        "owner": FHIR_Reference,
        # Principal physical location where the this task is performed.
        "location": FHIR_Reference,
        # A description or code indicating why this task needs to be performed.
        "reasonCode": FHIR_CodeableConcept,
        # A resource reference indicating why this task needs to be performed.
        "reasonReference": FHIR_Reference,
        # Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be relevant to the Task.
        "insurance": List[FHIR_Reference],
        # Free-text information captured about the task as it progresses.
        "note": List[FHIR_Annotation],
        # Links to Provenance records for past versions of this Task that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the task.
        "relevantHistory": List[FHIR_Reference],
        # If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actioned.
        "restriction": FHIR_Task_Restriction,
        # Additional information that may be needed in the execution of the task.
        "input": List[FHIR_Task_Input],
        # Outputs produced by the Task.
        "output": List[FHIR_Task_Output],
    },
    total=False,
)
