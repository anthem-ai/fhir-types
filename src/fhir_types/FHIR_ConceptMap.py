from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ConceptMap_Group import FHIR_ConceptMap_Group
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
FHIR_ConceptMap = TypedDict(
    "FHIR_ConceptMap",
    {
        # This is a ConceptMap resource
        "resourceType": Literal["ConceptMap"],
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
        # An absolute URI that is used to identify this concept map when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this concept map is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the concept map is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # A formal identifier that is used to identify this concept map when it is represented in other formats, or referenced in a specification, model, design or an instance.
        "identifier": FHIR_Identifier,
        # The identifier that is used to identify this version of the concept map when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the concept map author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the concept map. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the concept map.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The status of this concept map. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this concept map is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The date  (and optionally time) when the concept map was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the concept map changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the concept map.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the concept map from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate concept map instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the concept map is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this concept map is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # A copyright statement relating to the concept map and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the concept map.
        "copyright": FHIR_markdown,
        # Extensions for copyright
        "_copyright": FHIR_Element,
        # Identifier for the source value set that contains the concepts that are being mapped and provides context for the mappings.
        "sourceUri": str,
        # Extensions for sourceUri
        "_sourceUri": FHIR_Element,
        # Identifier for the source value set that contains the concepts that are being mapped and provides context for the mappings.
        "sourceCanonical": str,
        # Extensions for sourceCanonical
        "_sourceCanonical": FHIR_Element,
        # The target value set provides context for the mappings. Note that the mapping is made between concepts, not between value sets, but the value set provides important context about how the concept mapping choices are made.
        "targetUri": str,
        # Extensions for targetUri
        "_targetUri": FHIR_Element,
        # The target value set provides context for the mappings. Note that the mapping is made between concepts, not between value sets, but the value set provides important context about how the concept mapping choices are made.
        "targetCanonical": str,
        # Extensions for targetCanonical
        "_targetCanonical": FHIR_Element,
        # A group of mappings that all have the same source and target system.
        "group": List[FHIR_ConceptMap_Group],
    },
    total=False,
)
