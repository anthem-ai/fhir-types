from typing import Any, List, Literal, TypedDict

from .FHIR_ActivityDefinition_DynamicValue import FHIR_ActivityDefinition_DynamicValue
from .FHIR_ActivityDefinition_Participant import FHIR_ActivityDefinition_Participant
from .FHIR_Age import FHIR_Age
from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_date import FHIR_date
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Dosage import FHIR_Dosage
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
FHIR_ActivityDefinition = TypedDict(
    "FHIR_ActivityDefinition",
    {
        # This is a ActivityDefinition resource
        "resourceType": Literal["ActivityDefinition"],
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
        # An absolute URI that is used to identify this activity definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this activity definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the activity definition is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # A formal identifier that is used to identify this activity definition when it is represented in other formats, or referenced in a specification, model, design or an instance.
        "identifier": List[FHIR_Identifier],
        # The identifier that is used to identify this version of the activity definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the activity definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. To provide a version consistent with the Decision Support Service specification, use the format Major.Minor.Revision (e.g. 1.0.0). For more information on versioning knowledge assets, refer to the Decision Support Service specification. Note that a version is required for non-experimental active assets.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the activity definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the activity definition.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # An explanatory or alternate title for the activity definition giving additional information about its content.
        "subtitle": FHIR_string,
        # Extensions for subtitle
        "_subtitle": FHIR_Element,
        # The status of this activity definition. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this activity definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # A code or group definition that describes the intended subject of the activity being defined.
        "subjectCodeableConcept": FHIR_CodeableConcept,
        # A code or group definition that describes the intended subject of the activity being defined.
        "subjectReference": FHIR_Reference,
        # The date  (and optionally time) when the activity definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the activity definition changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the activity definition.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the activity definition from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate activity definition instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the activity definition is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this activity definition is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # A detailed description of how the activity definition is used from a clinical perspective.
        "usage": FHIR_string,
        # Extensions for usage
        "_usage": FHIR_Element,
        # A copyright statement relating to the activity definition and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the activity definition.
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
        # The period during which the activity definition content was or is planned to be in active use.
        "effectivePeriod": FHIR_Period,
        # Descriptive topics related to the content of the activity. Topics provide a high-level categorization of the activity that can be useful for filtering and searching.
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
        # A reference to a Library resource containing any formal logic used by the activity definition.
        "library": List[FHIR_canonical],
        # A description of the kind of resource the activity definition is representing. For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest. Typically, but not always, this is a Request resource.
        "kind": FHIR_code,
        # Extensions for kind
        "_kind": FHIR_Element,
        # A profile to which the target of the activity definition is expected to conform.
        "profile": FHIR_canonical,
        # Detailed description of the type of activity; e.g. What lab test, what procedure, what kind of encounter.
        "code": FHIR_CodeableConcept,
        # Indicates the level of authority/intentionality associated with the activity and where the request should fit into the workflow chain.
        "intent": FHIR_code,
        # Extensions for intent
        "_intent": FHIR_Element,
        # Indicates how quickly the activity  should be addressed with respect to other requests.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # Set this to true if the definition is to indicate that a particular activity should NOT be performed. If true, this element should be interpreted to reinforce a negative coding. For example NPO as a code with a doNotPerform of true would still indicate to NOT perform the action.
        "doNotPerform": FHIR_boolean,
        # Extensions for doNotPerform
        "_doNotPerform": FHIR_Element,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingTiming": FHIR_Timing,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingDateTime": str,
        # Extensions for timingDateTime
        "_timingDateTime": FHIR_Element,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingAge": FHIR_Age,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingPeriod": FHIR_Period,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingRange": FHIR_Range,
        # The period, timing or frequency upon which the described activity is to occur.
        "timingDuration": FHIR_Duration,
        # Identifies the facility where the activity will occur; e.g. home, hospital, specific clinic, etc.
        "location": FHIR_Reference,
        # Indicates who should participate in performing the action described.
        "participant": List[FHIR_ActivityDefinition_Participant],
        # Identifies the food, drug or other product being consumed or supplied in the activity.
        "productReference": FHIR_Reference,
        # Identifies the food, drug or other product being consumed or supplied in the activity.
        "productCodeableConcept": FHIR_CodeableConcept,
        # Identifies the quantity expected to be consumed at once (per dose, per meal, etc.).
        "quantity": FHIR_Quantity,
        # Provides detailed dosage instructions in the same way that they are described for MedicationRequest resources.
        "dosage": List[FHIR_Dosage],
        # Indicates the sites on the subject's body where the procedure should be performed (I.e. the target sites).
        "bodySite": List[FHIR_CodeableConcept],
        # Defines specimen requirements for the action to be performed, such as required specimens for a lab test.
        "specimenRequirement": List[FHIR_Reference],
        # Defines observation requirements for the action to be performed, such as body weight or surface area.
        "observationRequirement": List[FHIR_Reference],
        # Defines the observations that are expected to be produced by the action.
        "observationResultRequirement": List[FHIR_Reference],
        # A reference to a StructureMap resource that defines a transform that can be executed to produce the intent resource using the ActivityDefinition instance as the input.
        "transform": FHIR_canonical,
        # Dynamic values that will be evaluated to produce values for elements of the resulting resource. For example, if the dosage of a medication must be computed based on the patient's weight, a dynamic value would be used to specify an expression that calculated the weight, and the path on the request resource that would contain the result.
        "dynamicValue": List[FHIR_ActivityDefinition_DynamicValue],
    },
    total=False,
)
