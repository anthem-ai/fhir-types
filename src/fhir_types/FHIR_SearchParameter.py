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
from .FHIR_SearchParameter_Component import FHIR_SearchParameter_Component
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# A search parameter that defines a named search item that can be used to search/filter on a resource.
FHIR_SearchParameter = TypedDict(
    "FHIR_SearchParameter",
    {
        # This is a SearchParameter resource
        "resourceType": Literal["SearchParameter"],
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
        # An absolute URI that is used to identify this search parameter when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this search parameter is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the search parameter is stored on different servers.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # The identifier that is used to identify this version of the search parameter when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the search parameter author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # A natural language name identifying the search parameter. This name should be usable as an identifier for the module by machine processing applications such as code generation.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Where this search parameter is originally defined. If a derivedFrom is provided, then the details in the search parameter must be consistent with the definition from which it is defined. i.e. the parameter should have the same meaning, and (usually) the functionality should be a proper subset of the underlying search parameter.
        "derivedFrom": FHIR_canonical,
        # The status of this search parameter. Enables tracking the life-cycle of the content.
        "status": Literal["draft", "active", "retired", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # A Boolean value to indicate that this search parameter is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.
        "experimental": FHIR_boolean,
        # Extensions for experimental
        "_experimental": FHIR_Element,
        # The date  (and optionally time) when the search parameter was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the search parameter changes.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The name of the organization or individual that published the search parameter.
        "publisher": FHIR_string,
        # Extensions for publisher
        "_publisher": FHIR_Element,
        # Contact details to assist a user in finding and communicating with the publisher.
        "contact": List[FHIR_ContactDetail],
        # And how it used.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate search parameter instances.
        "useContext": List[FHIR_UsageContext],
        # A legal or geographic region in which the search parameter is intended to be used.
        "jurisdiction": List[FHIR_CodeableConcept],
        # Explanation of why this search parameter is needed and why it has been designed as it has.
        "purpose": FHIR_markdown,
        # Extensions for purpose
        "_purpose": FHIR_Element,
        # The code used in the URL or the parameter name in a parameters resource for this search parameter.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # The base resource type(s) that this search parameter can be used against.
        "base": List[FHIR_code],
        # Extensions for base
        "_base": List[FHIR_Element],
        # The type of value that a search parameter may contain, and how the content is interpreted.
        "type": Literal[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
            "special",
        ],
        # Extensions for type
        "_type": FHIR_Element,
        # A FHIRPath expression that returns a set of elements for the search parameter.
        "expression": FHIR_string,
        # Extensions for expression
        "_expression": FHIR_Element,
        # An XPath expression that returns a set of elements for the search parameter.
        "xpath": FHIR_string,
        # Extensions for xpath
        "_xpath": FHIR_Element,
        # How the search parameter relates to the set of elements returned by evaluating the xpath query.
        "xpathUsage": Literal["normal", "phonetic", "nearby", "distance", "other"],
        # Extensions for xpathUsage
        "_xpathUsage": FHIR_Element,
        # Types of resource (if a resource is referenced).
        "target": List[FHIR_code],
        # Extensions for target
        "_target": List[FHIR_Element],
        # Whether multiple values are allowed for each time the parameter exists. Values are separated by commas, and the parameter matches if any of the values match.
        "multipleOr": FHIR_boolean,
        # Extensions for multipleOr
        "_multipleOr": FHIR_Element,
        # Whether multiple parameters are allowed - e.g. more than one parameter with the same name. The search matches if all the parameters match.
        "multipleAnd": FHIR_boolean,
        # Extensions for multipleAnd
        "_multipleAnd": FHIR_Element,
        # Comparators supported for the search parameter.
        "comparator": List[
            Literal["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"]
        ],
        # Extensions for comparator
        "_comparator": List[FHIR_Element],
        # A modifier supported for the search parameter.
        "modifier": List[
            Literal[
                "missing",
                "exact",
                "contains",
                "not",
                "text",
                "in",
                "not-in",
                "below",
                "above",
                "type",
                "identifier",
                "ofType",
            ]
        ],
        # Extensions for modifier
        "_modifier": List[FHIR_Element],
        # Contains the names of any search parameters which may be chained to the containing search parameter. Chained parameters may be added to search parameters of type reference and specify that resources will only be returned if they contain a reference to a resource which matches the chained parameter value. Values for this field should be drawn from SearchParameter.code for a parameter on the target resource type.
        "chain": List[FHIR_string],
        # Extensions for chain
        "_chain": List[FHIR_Element],
        # Used to define the parts of a composite search parameter.
        "component": List[FHIR_SearchParameter_Component],
    },
    total=False,
)
