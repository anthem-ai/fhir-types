from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_CodeSystem_Concept import FHIR_CodeSystem_Concept
from .FHIR_CodeSystem_Filter import FHIR_CodeSystem_Filter
from .FHIR_CodeSystem_Property import FHIR_CodeSystem_Property
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
FHIR_CodeSystem = TypedDict(
    "FHIR_CodeSystem",
    {
        # This is a CodeSystem resource
        "resourceType": Literal["CodeSystem"],
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
        # An absolute URI that is used to identify this code system when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this code system is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the code system is stored on different servers. This is used in [Coding](datatypes.html#Coding).system.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # A formal identifier that is used to identify this code system when it is represented in other formats, or referenced in a specification, model, design or an instance.
        "identifier": List[FHIR_Identifier],
        # The identifier that is used to identify this version of the code system when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the code system author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. This is used in [Coding](datatypes.html#Coding).version.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the code system. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the code system.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The date (and optionally time) when the code system resource was created or revised.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this code system is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The date  (and optionally time) when the code system was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the code system changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the code system.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the code system from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate code system instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the code system is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this code system is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # A copyright statement relating to the code system and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the code system.
        "copyright": FHIR_markdown,
        # Extensions for copyright
        "_copyright": FHIR_Element,
        # If code comparison is case sensitive when codes within this system are compared to each other.
        "caseSensitive": FHIR_boolean,
        # Extensions for caseSensitive
        "_caseSensitive": FHIR_Element,
        # Canonical reference to the value set that contains the entire code system.
        "valueSet": FHIR_canonical,
        # The meaning of the hierarchy of concepts as represented in this resource.
        "hierarchyMeaning": Literal["grouped-by", "is-a", "part-of", "classified-with"],
        # Extensions for hierarchyMeaning
        "_hierarchyMeaning": FHIR_Element,
        # The code system defines a compositional (post-coordination) grammar.
        "compositional": FHIR_boolean,
        # Extensions for compositional
        "_compositional": FHIR_Element,
        # This flag is used to signify that the code system does not commit to concept permanence across versions. If true, a version must be specified when referencing this code system.
        "versionNeeded": FHIR_boolean,
        # Extensions for versionNeeded
        "_versionNeeded": FHIR_Element,
        # The extent of the content of the code system (the concepts and codes it defines) are represented in this resource instance.
        "content": Literal[
            "not-present", "example", "fragment", "complete", "supplement"
        ],
        # Extensions for content
        "_content": FHIR_Element,
        # The canonical URL of the code system that this code system supplement is adding designations and properties to.
        "supplements": FHIR_canonical,
        # The total number of concepts defined by the code system. Where the code system has a compositional grammar, the basis of this count is defined by the system steward.
        "count": FHIR_unsignedInt,
        # Extensions for count
        "_count": FHIR_Element,
        # A filter that can be used in a value set compose statement when selecting concepts using a filter.
        "filter": List[FHIR_CodeSystem_Filter],
        # A property defines an additional slot through which additional information can be provided about a concept.
        "property": List[FHIR_CodeSystem_Property],
        # Concepts that are in the code system. The concept definitions are inherently hierarchical, but the definitions must be consulted to determine what the meanings of the hierarchical relationships are.
        "concept": List[FHIR_CodeSystem_Concept],
    },
    total=False,
)
