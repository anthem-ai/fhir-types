from typing import Any, List, Literal, TypedDict

from .FHIR_Bundle_Entry import FHIR_Bundle_Entry
from .FHIR_Bundle_Link import FHIR_Bundle_Link
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Signature import FHIR_Signature
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_uri import FHIR_uri

# A container for a collection of resources.
FHIR_Bundle = TypedDict(
    "FHIR_Bundle",
    {
        # This is a Bundle resource
        "resourceType": Literal["Bundle"],
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
        # A persistent identifier for the bundle that won't change as a bundle is copied from server to server.
        "identifier": FHIR_Identifier,
        # Indicates the purpose of this bundle - how it is intended to be used.
        "type": Literal[
            "document",
            "message",
            "transaction",
            "transaction-response",
            "batch",
            "batch-response",
            "history",
            "searchset",
            "collection",
        ],
        # Extensions for type
        "_type": FHIR_Element,
        # The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.
        "timestamp": FHIR_instant,
        # Extensions for timestamp
        "_timestamp": FHIR_Element,
        # If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.
        "total": FHIR_unsignedInt,
        # Extensions for total
        "_total": FHIR_Element,
        # A series of links that provide context to this bundle.
        "link": List[FHIR_Bundle_Link],
        # An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).
        "entry": List[FHIR_Bundle_Entry],
        # Digital Signature - base64 encoded. XML-DSig or a JWT.
        "signature": FHIR_Signature,
    },
    total=False,
)
