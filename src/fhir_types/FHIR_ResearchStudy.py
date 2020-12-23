from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_ResearchStudy_Arm import FHIR_ResearchStudy_Arm
from .FHIR_ResearchStudy_Objective import FHIR_ResearchStudy_Objective
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
FHIR_ResearchStudy = TypedDict(
    "FHIR_ResearchStudy",
    {
        # This is a ResearchStudy resource
        "resourceType": Literal["ResearchStudy"],
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
        # Identifiers assigned to this research study by the sponsor or other systems.
        "identifier": List[FHIR_Identifier],
        # A short, descriptive user-friendly label for the study.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The set of steps expected to be performed as part of the execution of the study.
        "protocol": List[FHIR_Reference],
        # A larger research study of which this particular study is a component or step.
        "partOf": List[FHIR_Reference],
        # The current state of the study.
        "status": Literal[
            "active",
            "administratively-completed",
            "approved",
            "closed-to-accrual",
            "closed-to-accrual-and-intervention",
            "completed",
            "disapproved",
            "in-review",
            "temporarily-closed-to-accrual",
            "temporarily-closed-to-accrual-and-intervention",
            "withdrawn",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The type of study based upon the intent of the study's activities. A classification of the intent of the study.
        "primaryPurposeType": FHIR_CodeableConcept,
        # The stage in the progression of a therapy from initial experimental use in humans in clinical trials to post-market evaluation.
        "phase": FHIR_CodeableConcept,
        # Codes categorizing the type of study such as investigational vs. observational, type of blinding, type of randomization, safety vs. efficacy, etc.
        "category": List[FHIR_CodeableConcept],
        # The medication(s), food(s), therapy(ies), device(s) or other concerns or interventions that the study is seeking to gain more information about.
        "focus": List[FHIR_CodeableConcept],
        # The condition that is the focus of the study.  For example, In a study to examine risk factors for Lupus, might have as an inclusion criterion "healthy volunteer", but the target condition code would be a Lupus SNOMED code.
        "condition": List[FHIR_CodeableConcept],
        # Contact details to assist a user in learning more about or engaging with the study.
        "contact": List[FHIR_ContactDetail],
        # Citations, references and other related documents.
        "relatedArtifact": List[FHIR_RelatedArtifact],
        # Key terms to aid in searching for or filtering the study.
        "keyword": List[FHIR_CodeableConcept],
        # Indicates a country, state or other region where the study is taking place.
        "location": List[FHIR_CodeableConcept],
        # A full description of how the study is being conducted.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # Reference to a Group that defines the criteria for and quantity of subjects participating in the study.  E.g. " 200 female Europeans between the ages of 20 and 45 with early onset diabetes".
        "enrollment": List[FHIR_Reference],
        # Identifies the start date and the expected (or actual, depending on status) end date for the study.
        "period": FHIR_Period,
        # An organization that initiates the investigation and is legally responsible for the study.
        "sponsor": FHIR_Reference,
        # A researcher in a study who oversees multiple aspects of the study, such as concept development, protocol writing, protocol submission for IRB approval, participant recruitment, informed consent, data collection, analysis, interpretation and presentation.
        "principalInvestigator": FHIR_Reference,
        # A facility in which study activities are conducted.
        "site": List[FHIR_Reference],
        # A description and/or code explaining the premature termination of the study.
        "reasonStopped": FHIR_CodeableConcept,
        # Comments made about the study by the performer, subject or other participants.
        "note": List[FHIR_Annotation],
        # Describes an expected sequence of events for one of the participants of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up.
        "arm": List[FHIR_ResearchStudy_Arm],
        # A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.
        "objective": List[FHIR_ResearchStudy_Objective],
    },
    total=False,
)
