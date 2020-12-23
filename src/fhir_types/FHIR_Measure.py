from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_date import FHIR_date
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Measure_Group import FHIR_Measure_Group
from .FHIR_Measure_SupplementalData import FHIR_Measure_SupplementalData
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# The Measure resource provides the definition of a quality measure.
FHIR_Measure = TypedDict(
    "FHIR_Measure",
    {
        # This is a Measure resource
        "resourceType": Literal["Measure"],
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
        # An absolute URI that is used to identify this measure when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this measure is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the measure is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # A formal identifier that is used to identify this measure when it is represented in other formats, or referenced in a specification, model, design or an instance.
        "identifier": List[FHIR_Identifier],
        # The identifier that is used to identify this version of the measure when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the measure author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. To provide a version consistent with the Decision Support Service specification, use the format Major.Minor.Revision (e.g. 1.0.0). For more information on versioning knowledge assets, refer to the Decision Support Service specification. Note that a version is required for non-experimental active artifacts.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the measure. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the measure.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # An explanatory or alternate title for the measure giving additional information about its content.
        "subtitle": FHIR_string,
        # Extensions for subtitle
        "_subtitle": FHIR_Element,
        # The status of this measure. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this measure is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The intended subjects for the measure. If this element is not provided, a Patient subject is assumed, but the subject of the measure can be anything.
        "subjectCodeableConcept": FHIR_CodeableConcept,
        # The intended subjects for the measure. If this element is not provided, a Patient subject is assumed, but the subject of the measure can be anything.
        "subjectReference": FHIR_Reference,
        # The date  (and optionally time) when the measure was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the measure changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the measure.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the measure from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate measure instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the measure is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this measure is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # A detailed description, from a clinical perspective, of how the measure is used.
        "usage": FHIR_string,
        # Extensions for usage
        "_usage": FHIR_Element,
        # A copyright statement relating to the measure and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the measure.
        "copyright": FHIR_markdown,
        # Extensions for copyright
        "_copyright": FHIR_Element,
        # The date on which the resource content was approved by the publisher. Approval happens once when the content is officially approved for usage.
        "approvalDate": FHIR_date,
        # Extensions for approvalDate
        "_approvalDate": FHIR_Element,
        # The date on which the resource content was last reviewed. Review happens periodically after approval but does not change the original approval date.
        "lastReviewDate": FHIR_date,
        # Extensions for lastReviewDate
        "_lastReviewDate": FHIR_Element,
        # The period during which the measure content was or is planned to be in active use.
        "effectivePeriod": FHIR_Period,
        # Descriptive topics related to the content of the measure. Topics provide a high-level categorization grouping types of measures that can be useful for filtering and searching.
        "topic": List[FHIR_CodeableConcept],
        # An individiual or organization primarily involved in the creation and maintenance of the content.
        "author": List[FHIR_ContactDetail],
        # An individual or organization primarily responsible for internal coherence of the content.
        "editor": List[FHIR_ContactDetail],
        # An individual or organization primarily responsible for review of some aspect of the content.
        "reviewer": List[FHIR_ContactDetail],
        # An individual or organization responsible for officially endorsing the content for use in some setting.
        "endorser": List[FHIR_ContactDetail],
        # Related artifacts such as additional documentation, justification, or bibliographic references.
        "relatedArtifact": List[FHIR_RelatedArtifact],
        # A reference to a Library resource containing the formal logic used by the measure.
        "library": List[FHIR_canonical],
        # Notices and disclaimers regarding the use of the measure or related to intellectual property (such as code systems) referenced by the measure.
        "disclaimer": FHIR_markdown,
        # Extensions for disclaimer
        "_disclaimer": FHIR_Element,
        # Indicates how the calculation is performed for the measure, including proportion, ratio, continuous-variable, and cohort. The value set is extensible, allowing additional measure scoring types to be represented.
        "scoring": FHIR_CodeableConcept,
        # If this is a composite measure, the scoring method used to combine the component measures to determine the composite score.
        "compositeScoring": FHIR_CodeableConcept,
        # Indicates whether the measure is used to examine a process, an outcome over time, a patient-reported outcome, or a structure measure such as utilization.
        "type": List[FHIR_CodeableConcept],
        # A description of the risk adjustment factors that may impact the resulting score for the measure and how they may be accounted for when computing and reporting measure results.
        "riskAdjustment": FHIR_string,
        # Extensions for riskAdjustment
        "_riskAdjustment": FHIR_Element,
        # Describes how to combine the information calculated, based on logic in each of several populations, into one summarized result.
        "rateAggregation": FHIR_string,
        # Extensions for rateAggregation
        "_rateAggregation": FHIR_Element,
        # Provides a succinct statement of the need for the measure. Usually includes statements pertaining to importance criterion: impact, gap in care, and evidence.
        "rationale": FHIR_markdown,
        # Extensions for rationale
        "_rationale": FHIR_Element,
        # Provides a summary of relevant clinical guidelines or other clinical recommendations supporting the measure.
        "clinicalRecommendationStatement": FHIR_markdown,
        # Extensions for clinicalRecommendationStatement
        "_clinicalRecommendationStatement": FHIR_Element,
        # Information on whether an increase or decrease in score is the preferred result (e.g., a higher score indicates better quality OR a lower score indicates better quality OR quality is within a range).
        "improvementNotation": FHIR_CodeableConcept,
        # Provides a description of an individual term used within the measure.
        "definition": List[FHIR_markdown],
        # Extensions for definition
        "_definition": List[FHIR_Element],
        # Additional guidance for the measure including how it can be used in a clinical context, and the intent of the measure.
        "guidance": FHIR_markdown,
        # Extensions for guidance
        "_guidance": FHIR_Element,
        # A group of population criteria for the measure.
        "group": List[FHIR_Measure_Group],
        # The supplemental data criteria for the measure report, specified as either the name of a valid CQL expression within a referenced library, or a valid FHIR Resource Path.
        "supplementalData": List[FHIR_Measure_SupplementalData],
    },
    total=False,
)
