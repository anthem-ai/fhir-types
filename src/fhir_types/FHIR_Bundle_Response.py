from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_instant import FHIR_instant
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A container for a collection of resources.
FHIR_Bundle_Response = TypedDict(
    "FHIR_Bundle_Response",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.
        "status": FHIR_string,
        # Extensions for status
        "_status": FHIR_Element,
        # The location header created by processing this operation, populated if the operation returns a location.
        "location": FHIR_uri,
        # Extensions for location
        "_location": FHIR_Element,
        # The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).
        "etag": FHIR_string,
        # Extensions for etag
        "_etag": FHIR_Element,
        # The date/time that the resource was modified on the server.
        "lastModified": FHIR_instant,
        # Extensions for lastModified
        "_lastModified": FHIR_Element,
        # An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.
        "outcome": Any,
    },
    total=False,
)
