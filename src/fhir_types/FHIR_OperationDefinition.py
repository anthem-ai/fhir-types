from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_OperationDefinition_Overload import FHIR_OperationDefinition_Overload
from .FHIR_OperationDefinition_Parameter import FHIR_OperationDefinition_Parameter
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
FHIR_OperationDefinition = TypedDict(
    "FHIR_OperationDefinition",
    {
        # This is a OperationDefinition resource
        "resourceType": Literal["OperationDefinition"],
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
        # An absolute URI that is used to identify this operation definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this operation definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the operation definition is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # The identifier that is used to identify this version of the operation definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the operation definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the operation definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A short, descriptive, user-friendly title for the operation definition.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The status of this operation definition. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # Whether this is an operation or a named query.
        "kind": Literal["operation", "query"],
        # Extensions for kind
        "_kind": FHIR_Element,
        # A Boolean value to indicate that this operation definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The date  (and optionally time) when the operation definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the operation definition changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the operation definition.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # A free text natural language description of the operation definition from a consumer's perspective.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate operation definition instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the operation definition is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this operation definition is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # Whether the operation affects state. Side effects such as producing audit trail entries do not count as 'affecting  state'.
        "affectsState": FHIR_boolean,
        # Extensions for affectsState
        "_affectsState": FHIR_Element,
        # The name used to invoke the operation.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # Additional information about how to use this operation or named query.
        "comment": FHIR_markdown,
        # Extensions for comment
        "_comment": FHIR_Element,
        # Indicates that this operation definition is a constraining profile on the base.
        "base": FHIR_canonical,
        # The types on which this operation can be executed.
        "resource": List[FHIR_code],
        # Extensions for resource
        "_resource": List[FHIR_Element],
        # Indicates whether this operation or named query can be invoked at the system level (e.g. without needing to choose a resource type for the context).
        "system": FHIR_boolean,
        # Extensions for system
        "_system": FHIR_Element,
        # Indicates whether this operation or named query can be invoked at the resource type level for any given resource type level (e.g. without needing to choose a specific resource id for the context).
        "type": FHIR_boolean,
        # Extensions for type
        "_type": FHIR_Element,
        # Indicates whether this operation can be invoked on a particular instance of one of the given types.
        "instance": FHIR_boolean,
        # Extensions for instance
        "_instance": FHIR_Element,
        # Additional validation information for the in parameters - a single profile that covers all the parameters. The profile is a constraint on the parameters resource as a whole.
        "inputProfile": FHIR_canonical,
        # Additional validation information for the out parameters - a single profile that covers all the parameters. The profile is a constraint on the parameters resource.
        "outputProfile": FHIR_canonical,
        # The parameters for the operation/query.
        "parameter": List[FHIR_OperationDefinition_Parameter],
        # Defines an appropriate combination of parameters to use when invoking this operation, to help code generators when generating overloaded parameter sets for this operation.
        "overload": List[FHIR_OperationDefinition_Overload],
    },
    total=False,
)
