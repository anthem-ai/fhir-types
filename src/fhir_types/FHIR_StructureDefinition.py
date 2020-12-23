from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_string import FHIR_string
from .FHIR_StructureDefinition_Context import FHIR_StructureDefinition_Context
from .FHIR_StructureDefinition_Differential import FHIR_StructureDefinition_Differential
from .FHIR_StructureDefinition_Mapping import FHIR_StructureDefinition_Mapping
from .FHIR_StructureDefinition_Snapshot import FHIR_StructureDefinition_Snapshot
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.
FHIR_StructureDefinition = TypedDict(
    "FHIR_StructureDefinition",
    {
        # This is a StructureDefinition resource
        "resourceType": Literal["StructureDefinition"],
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
        # An absolute URI that is used to identify this structure definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this structure definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the structure definition is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # A formal identifier that is used to identify this structure definition when it is represented in other formats, or referenced in a specification, model, design or an instance.
        "identifier": List[FHIR_Identifier],
        # The identifier that is used to identify this version of the structure definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the structure definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the structure definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the structure definition.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The status of this structure definition. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this structure definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The date  (and optionally time) when the structure definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the structure definition changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the structure definition.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the structure definition from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate structure definition instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the structure definition is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this structure definition is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # A copyright statement relating to the structure definition and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the structure definition.
        "copyright": FHIR_markdown,
        # Extensions for copyright
        "_copyright": FHIR_Element,
        # A set of key words or terms from external terminologies that may be used to assist with indexing and searching of templates nby describing the use of this structure definition, or the content it describes.
        "keyword": List[FHIR_Coding],
        # The version of the FHIR specification on which this StructureDefinition is based - this is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.
        "fhirVersion": Literal[
            "0.01",
            "0.05",
            "0.06",
            "0.11",
            "0.0.80",
            "0.0.81",
            "0.0.82",
            "0.4.0",
            "0.5.0",
            "1.0.0",
            "1.0.1",
            "1.0.2",
            "1.1.0",
            "1.4.0",
            "1.6.0",
            "1.8.0",
            "3.0.0",
            "3.0.1",
            "3.3.0",
            "3.5.0",
            "4.0.0",
            "4.0.1",
        ],
        # Extensions for fhirVersion
        "_fhirVersion": FHIR_Element,
        # An external specification that the content is mapped to.
        "mapping": List[FHIR_StructureDefinition_Mapping],
        # Defines the kind of structure that this definition is describing.
        "kind": Literal["primitive-type", "complex-type", "resource", "logical"],
        # Extensions for kind
        "_kind": FHIR_Element,
        # Whether structure this definition describes is abstract or not  - that is, whether the structure is not intended to be instantiated. For Resources and Data types, abstract types will never be exchanged  between systems.
        "abstract": FHIR_boolean,
        # Extensions for abstract
        "_abstract": FHIR_Element,
        # Identifies the types of resource or data type elements to which the extension can be applied.
        "context": List[FHIR_StructureDefinition_Context],
        # A set of rules as FHIRPath Invariants about when the extension can be used (e.g. co-occurrence variants for the extension). All the rules must be true.
        "contextInvariant": List[FHIR_string],
        # Extensions for contextInvariant
        "_contextInvariant": List[FHIR_Element],
        # The type this structure describes. If the derivation kind is 'specialization' then this is the master definition for a type, and there is always one of these (a data type, an extension, a resource, including abstract ones). Otherwise the structure definition is a constraint on the stated type (and in this case, the type cannot be an abstract type).  References are URLs that are relative to http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed in logical models.
        "type": FHIR_uri,
        # Extensions for type
        "_type": FHIR_Element,
        # An absolute URI that is the base structure from which this type is derived, either by specialization or constraint.
        "baseDefinition": FHIR_canonical,
        # How the type relates to the baseDefinition.
        "derivation": Literal["specialization", "constraint"],
        # Extensions for derivation
        "_derivation": FHIR_Element,
        # A snapshot view is expressed in a standalone form that can be used and interpreted without considering the base StructureDefinition.
        "snapshot": FHIR_StructureDefinition_Snapshot,
        # A differential view is expressed relative to the base StructureDefinition - a statement of differences that it applies.
        "differential": FHIR_StructureDefinition_Differential,
    },
    total=False,
)
