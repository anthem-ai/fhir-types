from typing import Any, List, Literal, TypedDict

from .FHIR_base64Binary import FHIR_base64Binary
from .FHIR_code import FHIR_code
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_instant import FHIR_instant
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
FHIR_Signature = TypedDict(
    "FHIR_Signature",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # An indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the document.
        "type": List[FHIR_Coding],
        # When the digital signature was signed.
        "when": FHIR_instant,
        # Extensions for when
        "_when": FHIR_Element,
        # A reference to an application-usable description of the identity that signed  (e.g. the signature used their private key).
        "who": FHIR_Reference,
        # A reference to an application-usable description of the identity that is represented by the signature.
        "onBehalfOf": FHIR_Reference,
        # A mime type that indicates the technical format of the target resources signed by the signature.
        "targetFormat": FHIR_code,
        # Extensions for targetFormat
        "_targetFormat": FHIR_Element,
        # A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etc.
        "sigFormat": FHIR_code,
        # Extensions for sigFormat
        "_sigFormat": FHIR_Element,
        # The base64 encoding of the Signature content. When signature is not recorded electronically this element would be empty.
        "data": FHIR_base64Binary,
        # Extensions for data
        "_data": FHIR_Element,
    },
    total=False,
)
