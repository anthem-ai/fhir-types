from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_CapabilityStatement_Interaction import FHIR_CapabilityStatement_Interaction
from .FHIR_CapabilityStatement_Operation import FHIR_CapabilityStatement_Operation
from .FHIR_CapabilityStatement_SearchParam import FHIR_CapabilityStatement_SearchParam
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
FHIR_CapabilityStatement_Resource = TypedDict(
    "FHIR_CapabilityStatement_Resource",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A type of resource exposed via the restful interface.
        "type": FHIR_code,
        # Extensions for type
        "_type": FHIR_Element,
        # A specification of the profile that describes the solution's overall support for the resource, including any constraints on cardinality, bindings, lengths or other limitations. See further discussion in [Using Profiles](profiling.html#profile-uses).
        "profile": FHIR_canonical,
        # A list of profiles that represent different use cases supported by the system. For a server, "supported by the system" means the system hosts/produces a set of resources that are conformant to a particular profile, and allows clients that use its services to search using this profile and to find appropriate data. For a client, it means the system will search by this profile and process data according to the guidance implicit in the profile. See further discussion in [Using Profiles](profiling.html#profile-uses).
        "supportedProfile": List[FHIR_canonical],
        # Additional information about the resource type used by the system.
        "documentation": FHIR_markdown,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # Identifies a restful operation supported by the solution.
        "interaction": List[FHIR_CapabilityStatement_Interaction],
        # This field is set to no-version to specify that the system does not support (server) or use (client) versioning for this resource type. If this has some other value, the server must at least correctly track and populate the versionId meta-property on resources. If the value is 'versioned-update', then the server supports all the versioning features, including using e-tags for version integrity in the API.
        "versioning": Literal["no-version", "versioned", "versioned-update"],
        # Extensions for versioning
        "_versioning": FHIR_Element,
        # A flag for whether the server is able to return past versions as part of the vRead operation.
        "readHistory": FHIR_boolean,
        # Extensions for readHistory
        "_readHistory": FHIR_Element,
        # A flag to indicate that the server allows or needs to allow the client to create new identities on the server (that is, the client PUTs to a location where there is no existing resource). Allowing this operation means that the server allows the client to create new identities on the server.
        "updateCreate": FHIR_boolean,
        # Extensions for updateCreate
        "_updateCreate": FHIR_Element,
        # A flag that indicates that the server supports conditional create.
        "conditionalCreate": FHIR_boolean,
        # Extensions for conditionalCreate
        "_conditionalCreate": FHIR_Element,
        # A code that indicates how the server supports conditional read.
        "conditionalRead": Literal[
            "not-supported", "modified-since", "not-match", "full-support"
        ],
        # Extensions for conditionalRead
        "_conditionalRead": FHIR_Element,
        # A flag that indicates that the server supports conditional update.
        "conditionalUpdate": FHIR_boolean,
        # Extensions for conditionalUpdate
        "_conditionalUpdate": FHIR_Element,
        # A code that indicates how the server supports conditional delete.
        "conditionalDelete": Literal["not-supported", "single", "multiple"],
        # Extensions for conditionalDelete
        "_conditionalDelete": FHIR_Element,
        # A set of flags that defines how references are supported.
        "referencePolicy": List[
            Literal["literal", "logical", "resolves", "enforced", "local"]
        ],
        # Extensions for referencePolicy
        "_referencePolicy": List[FHIR_Element],
        # A list of _include values supported by the server.
        "searchInclude": List[FHIR_string],
        # Extensions for searchInclude
        "_searchInclude": List[FHIR_Element],
        # A list of _revinclude (reverse include) values supported by the server.
        "searchRevInclude": List[FHIR_string],
        # Extensions for searchRevInclude
        "_searchRevInclude": List[FHIR_Element],
        # Search parameters for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.
        "searchParam": List[FHIR_CapabilityStatement_SearchParam],
        # Definition of an operation or a named query together with its parameters and their meaning and type. Consult the definition of the operation for details about how to invoke the operation, and the parameters.
        "operation": List[FHIR_CapabilityStatement_Operation],
    },
    total=False,
)
