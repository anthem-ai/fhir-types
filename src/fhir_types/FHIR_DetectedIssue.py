from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_DetectedIssue_Evidence import FHIR_DetectedIssue_Evidence
from .FHIR_DetectedIssue_Mitigation import FHIR_DetectedIssue_Mitigation
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
FHIR_DetectedIssue = TypedDict(
    "FHIR_DetectedIssue",
    {
        # This is a DetectedIssue resource
        "resourceType": Literal["DetectedIssue"],
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
        # Business identifier associated with the detected issue record.
        "identifier": List[FHIR_Identifier],
        # Indicates the status of the detected issue.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Identifies the general type of issue identified.
        "code": FHIR_CodeableConcept,
        # Indicates the degree of importance associated with the identified issue based on the potential impact on the patient.
        "severity": Literal["high", "moderate", "low"],
        # Extensions for severity
        "_severity": FHIR_Element,
        # Indicates the patient whose record the detected issue is associated with.
        "patient": FHIR_Reference,
        # The date or period when the detected issue was initially identified.
        "identifiedDateTime": str,
        # Extensions for identifiedDateTime
        "_identifiedDateTime": FHIR_Element,
        # The date or period when the detected issue was initially identified.
        "identifiedPeriod": FHIR_Period,
        # Individual or device responsible for the issue being raised.  For example, a decision support application or a pharmacist conducting a medication review.
        "author": FHIR_Reference,
        # Indicates the resource representing the current activity or proposed activity that is potentially problematic.
        "implicated": List[FHIR_Reference],
        # Supporting evidence or manifestations that provide the basis for identifying the detected issue such as a GuidanceResponse or MeasureReport.
        "evidence": List[FHIR_DetectedIssue_Evidence],
        # A textual explanation of the detected issue.
        "detail": FHIR_string,
        # Extensions for detail
        "_detail": FHIR_Element,
        # The literature, knowledge-base or similar reference that describes the propensity for the detected issue identified.
        "reference": FHIR_uri,
        # Extensions for reference
        "_reference": FHIR_Element,
        # Indicates an action that has been taken or is committed to reduce or eliminate the likelihood of the risk identified by the detected issue from manifesting.  Can also reflect an observation of known mitigating factors that may reduce/eliminate the need for any action.
        "mitigation": List[FHIR_DetectedIssue_Mitigation],
    },
    total=False,
)
