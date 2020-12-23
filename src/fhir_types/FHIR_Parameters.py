from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Meta import FHIR_Meta
from .FHIR_Parameters_Parameter import FHIR_Parameters_Parameter
from .FHIR_uri import FHIR_uri

# This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
FHIR_Parameters = TypedDict(
    "FHIR_Parameters",
    {
        # This is a Parameters resource
        "resourceType": Literal["Parameters"],
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
        # A parameter passed to or received from the operation.
        "parameter": List[FHIR_Parameters_Parameter],
    },
    total=False,
)
