from typing import Any, List, Literal, TypedDict

from .FHIR_Age import FHIR_Age
from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Condition_Evidence import FHIR_Condition_Evidence
from .FHIR_Condition_Stage import FHIR_Condition_Stage
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
FHIR_Condition = TypedDict(
    "FHIR_Condition",
    {
        # This is a Condition resource
        "resourceType": Literal["Condition"],
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
        # Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # The clinical status of the condition.
        "clinicalStatus": FHIR_CodeableConcept,
        # The verification status to support the clinical status of the condition.
        "verificationStatus": FHIR_CodeableConcept,
        # A category assigned to the condition.
        "category": List[FHIR_CodeableConcept],
        # A subjective assessment of the severity of the condition as evaluated by the clinician.
        "severity": FHIR_CodeableConcept,
        # Identification of the condition, problem or diagnosis.
        "code": FHIR_CodeableConcept,
        # The anatomical location where this condition manifests itself.
        "bodySite": List[FHIR_CodeableConcept],
        # Indicates the patient or group who the condition record is associated with.
        "subject": FHIR_Reference,
        # The Encounter during which this Condition was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # Estimated or actual date or date-time  the condition began, in the opinion of the clinician.
        "onsetDateTime": str,
        # Extensions for onsetDateTime
        "_onsetDateTime": FHIR_Element,
        # Estimated or actual date or date-time  the condition began, in the opinion of the clinician.
        "onsetAge": FHIR_Age,
        # Estimated or actual date or date-time  the condition began, in the opinion of the clinician.
        "onsetPeriod": FHIR_Period,
        # Estimated or actual date or date-time  the condition began, in the opinion of the clinician.
        "onsetRange": FHIR_Range,
        # Estimated or actual date or date-time  the condition began, in the opinion of the clinician.
        "onsetString": str,
        # Extensions for onsetString
        "_onsetString": FHIR_Element,
        # The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.
        "abatementDateTime": str,
        # Extensions for abatementDateTime
        "_abatementDateTime": FHIR_Element,
        # The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.
        "abatementAge": FHIR_Age,
        # The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.
        "abatementPeriod": FHIR_Period,
        # The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.
        "abatementRange": FHIR_Range,
        # The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.
        "abatementString": str,
        # Extensions for abatementString
        "_abatementString": FHIR_Element,
        # The recordedDate represents when this particular Condition record was created in the system, which is often a system-generated date.
        "recordedDate": FHIR_dateTime,
        # Extensions for recordedDate
        "_recordedDate": FHIR_Element,
        # Individual who recorded the record and takes responsibility for its content.
        "recorder": FHIR_Reference,
        # Individual who is making the condition statement.
        "asserter": FHIR_Reference,
        # Clinical stage or grade of a condition. May include formal severity assessments.
        "stage": List[FHIR_Condition_Stage],
        # Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.
        "evidence": List[FHIR_Condition_Evidence],
        # Additional information about the Condition. This is a general notes/comments entry  for description of the Condition, its diagnosis and prognosis.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
