from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_QuestionnaireResponse_Item import FHIR_QuestionnaireResponse_Item
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
FHIR_QuestionnaireResponse = TypedDict(
    "FHIR_QuestionnaireResponse",
    {
        # This is a QuestionnaireResponse resource
        "resourceType": Literal["QuestionnaireResponse"],
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
        # A business identifier assigned to a particular completed (or partially completed) questionnaire.
        "identifier": FHIR_Identifier,
        # The order, proposal or plan that is fulfilled in whole or in part by this QuestionnaireResponse.  For example, a ServiceRequest seeking an intake assessment or a decision support recommendation to assess for post-partum depression.
        "basedOn": List[FHIR_Reference],
        # A procedure or observation that this questionnaire was performed as part of the execution of.  For example, the surgery a checklist was executed as part of.
        "partOf": List[FHIR_Reference],
        # The Questionnaire that defines and organizes the questions for which answers are being provided.
        "questionnaire": FHIR_canonical,
        # The position of the questionnaire response within its overall lifecycle.
        "status": Literal[
            "in-progress", "completed", "amended", "entered-in-error", "stopped"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The subject of the questionnaire response.  This could be a patient, organization, practitioner, device, etc.  This is who/what the answers apply to, but is not necessarily the source of information.
        "subject": FHIR_Reference,
        # The Encounter during which this questionnaire response was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # The date and/or time that this set of answers were last changed.
        "authored": FHIR_dateTime,
        # Extensions for authored
        "_authored": FHIR_Element,
        # Person who received the answers to the questions in the QuestionnaireResponse and recorded them in the system.
        "author": FHIR_Reference,
        # The person who answered the questions about the subject.
        "source": FHIR_Reference,
        # A group or question item from the original questionnaire for which answers are provided.
        "item": List[FHIR_QuestionnaireResponse_Item],
    },
    total=False,
)
