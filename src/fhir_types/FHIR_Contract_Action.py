from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Contract_Subject import FHIR_Contract_Subject
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_unsignedInt import FHIR_unsignedInt

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_Action = TypedDict(
    "FHIR_Contract_Action",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # True if the term prohibits the  action.
        "doNotPerform": FHIR_boolean,
        # Extensions for doNotPerform
        "_doNotPerform": FHIR_Element,
        # Activity or service obligation to be done or not done, performed or not performed, effectuated or not by this Contract term.
        "type": FHIR_CodeableConcept,
        # Entity of the action.
        "subject": List[FHIR_Contract_Subject],
        # Reason or purpose for the action stipulated by this Contract Provision.
        "intent": FHIR_CodeableConcept,
        # Id [identifier??] of the clause or question text related to this action in the referenced form or QuestionnaireResponse.
        "linkId": List[FHIR_string],
        # Extensions for linkId
        "_linkId": List[FHIR_Element],
        # Current state of the term action.
        "status": FHIR_CodeableConcept,
        # Encounter or Episode with primary association to specified term activity.
        "context": FHIR_Reference,
        # Id [identifier??] of the clause or question text related to the requester of this action in the referenced form or QuestionnaireResponse.
        "contextLinkId": List[FHIR_string],
        # Extensions for contextLinkId
        "_contextLinkId": List[FHIR_Element],
        # When action happens.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # When action happens.
        "occurrencePeriod": FHIR_Period,
        # When action happens.
        "occurrenceTiming": FHIR_Timing,
        # Who or what initiated the action and has responsibility for its activation.
        "requester": List[FHIR_Reference],
        # Id [identifier??] of the clause or question text related to the requester of this action in the referenced form or QuestionnaireResponse.
        "requesterLinkId": List[FHIR_string],
        # Extensions for requesterLinkId
        "_requesterLinkId": List[FHIR_Element],
        # The type of individual that is desired or required to perform or not perform the action.
        "performerType": List[FHIR_CodeableConcept],
        # The type of role or competency of an individual desired or required to perform or not perform the action.
        "performerRole": FHIR_CodeableConcept,
        # Indicates who or what is being asked to perform (or not perform) the ction.
        "performer": FHIR_Reference,
        # Id [identifier??] of the clause or question text related to the reason type or reference of this  action in the referenced form or QuestionnaireResponse.
        "performerLinkId": List[FHIR_string],
        # Extensions for performerLinkId
        "_performerLinkId": List[FHIR_Element],
        # Rationale for the action to be performed or not performed. Describes why the action is permitted or prohibited.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource whose existence justifies permitting or not permitting this action.
        "reasonReference": List[FHIR_Reference],
        # Describes why the action is to be performed or not performed in textual form.
        "reason": List[FHIR_string],
        # Extensions for reason
        "_reason": List[FHIR_Element],
        # Id [identifier??] of the clause or question text related to the reason type or reference of this  action in the referenced form or QuestionnaireResponse.
        "reasonLinkId": List[FHIR_string],
        # Extensions for reasonLinkId
        "_reasonLinkId": List[FHIR_Element],
        # Comments made about the term action made by the requester, performer, subject or other participants.
        "note": List[FHIR_Annotation],
        # Security labels that protects the action.
        "securityLabelNumber": List[FHIR_unsignedInt],
        # Extensions for securityLabelNumber
        "_securityLabelNumber": List[FHIR_Element],
    },
    total=False,
)
