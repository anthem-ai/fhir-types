from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_RiskAssessment_Prediction import FHIR_RiskAssessment_Prediction
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
FHIR_RiskAssessment = TypedDict(
    "FHIR_RiskAssessment",
    {
        # This is a RiskAssessment resource
        "resourceType": Literal["RiskAssessment"],
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
        # Business identifier assigned to the risk assessment.
        "identifier": List[FHIR_Identifier],
        # A reference to the request that is fulfilled by this risk assessment.
        "basedOn": FHIR_Reference,
        # A reference to a resource that this risk assessment is part of, such as a Procedure.
        "parent": FHIR_Reference,
        # The status of the RiskAssessment, using the same statuses as an Observation.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # The algorithm, process or mechanism used to evaluate the risk.
        "method": FHIR_CodeableConcept,
        # The type of the risk assessment performed.
        "code": FHIR_CodeableConcept,
        # The patient or group the risk assessment applies to.
        "subject": FHIR_Reference,
        # The encounter where the assessment was performed.
        "encounter": FHIR_Reference,
        # The date (and possibly time) the risk assessment was performed.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # The date (and possibly time) the risk assessment was performed.
        "occurrencePeriod": FHIR_Period,
        # For assessments or prognosis specific to a particular condition, indicates the condition being assessed.
        "condition": FHIR_Reference,
        # The provider or software application that performed the assessment.
        "performer": FHIR_Reference,
        # The reason the risk assessment was performed.
        "reasonCode": List[FHIR_CodeableConcept],
        # Resources supporting the reason the risk assessment was performed.
        "reasonReference": List[FHIR_Reference],
        # Indicates the source data considered as part of the assessment (for example, FamilyHistory, Observations, Procedures, Conditions, etc.).
        "basis": List[FHIR_Reference],
        # Describes the expected outcome for the subject.
        "prediction": List[FHIR_RiskAssessment_Prediction],
        # A description of the steps that might be taken to reduce the identified risk(s).
        "mitigation": FHIR_string,
        # Extensions for mitigation
        "_mitigation": FHIR_Element,
        # Additional comments about the risk assessment.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
