from typing import Any, List, Literal, TypedDict

from .FHIR_base64Binary import FHIR_base64Binary
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Meta import FHIR_Meta
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
FHIR_Binary = TypedDict(
    "FHIR_Binary",
    {
        # This is a Binary resource
        "resourceType": Literal["Binary"],
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
        # MimeType of the binary content represented as a standard MimeType (BCP 13).
        "contentType": FHIR_code,
        # Extensions for contentType
        "_contentType": FHIR_Element,
        # This element identifies another resource that can be used as a proxy of the security sensitivity to use when deciding and enforcing access control rules for the Binary resource. Given that the Binary resource contains very few elements that can be used to determine the sensitivity of the data and relationships to individuals, the referenced resource stands in as a proxy equivalent for this purpose. This referenced resource may be related to the Binary (e.g. Media, DocumentReference), or may be some non-related Resource purely as a security proxy. E.g. to identify that the binary resource relates to a patient, and access should only be granted to applications that have access to the patient.
        "securityContext": FHIR_Reference,
        # The actual content, base64 encoded.
        "data": FHIR_base64Binary,
        # Extensions for data
        "_data": FHIR_Element,
    },
    total=False,
)
