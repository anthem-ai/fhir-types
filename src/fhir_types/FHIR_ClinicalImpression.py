from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_ClinicalImpression_Finding import FHIR_ClinicalImpression_Finding
from .FHIR_ClinicalImpression_Investigation import FHIR_ClinicalImpression_Investigation
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
from .FHIR_uri import FHIR_uri

# A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
FHIR_ClinicalImpression = TypedDict(
    "FHIR_ClinicalImpression",
    {
        # This is a ClinicalImpression resource
        "resourceType": Literal["ClinicalImpression"],
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
        # Business identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # Identifies the workflow status of the assessment.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Captures the reason for the current state of the ClinicalImpression.
        "statusReason": FHIR_CodeableConcept,
        # Categorizes the type of clinical assessment performed.
        "code": FHIR_CodeableConcept,
        # A summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted it.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The patient or group of individuals assessed as part of this record.
        "subject": FHIR_Reference,
        # The Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # The point in time or period over which the subject was assessed.
        "effectiveDateTime": str,
        # Extensions for effectiveDateTime
        "_effectiveDateTime": FHIR_Element,
        # The point in time or period over which the subject was assessed.
        "effectivePeriod": FHIR_Period,
        # Indicates when the documentation of the assessment was complete.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The clinician performing the assessment.
        "assessor": FHIR_Reference,
        # A reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changes.
        "previous": FHIR_Reference,
        # A list of the relevant problems/conditions for a patient.
        "problem": List[FHIR_Reference],
        # One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.
        "investigation": List[FHIR_ClinicalImpression_Investigation],
        # Reference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosis.
        "protocol": List[FHIR_uri],
        # Extensions for protocol
        "_protocol": List[FHIR_Element],
        # A text summary of the investigations and the diagnosis.
        "summary": FHIR_string,
        # Extensions for summary
        "_summary": FHIR_Element,
        # Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.
        "finding": List[FHIR_ClinicalImpression_Finding],
        # Estimate of likely outcome.
        "prognosisCodeableConcept": List[FHIR_CodeableConcept],
        # RiskAssessment expressing likely outcome.
        "prognosisReference": List[FHIR_Reference],
        # Information supporting the clinical impression.
        "supportingInfo": List[FHIR_Reference],
        # Commentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appear.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
