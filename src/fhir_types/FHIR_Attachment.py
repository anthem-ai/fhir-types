from typing import Any, List, Literal, TypedDict

from .FHIR_base64Binary import FHIR_base64Binary
from .FHIR_code import FHIR_code
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_url import FHIR_url

# For referring to data content defined in other formats.
FHIR_Attachment = TypedDict(
    "FHIR_Attachment",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # Identifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriate.
        "contentType": FHIR_code,
        # Extensions for contentType
        "_contentType": FHIR_Element,
        # The human language of the content. The value can be any valid value according to BCP 47.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # The actual data of the attachment - a sequence of bytes, base64 encoded.
        "data": FHIR_base64Binary,
        # Extensions for data
        "_data": FHIR_Element,
        # A location where the data can be accessed.
        "url": FHIR_url,
        # Extensions for url
        "_url": FHIR_Element,
        # The number of bytes of data that make up this attachment (before base64 encoding, if that is done).
        "size": FHIR_unsignedInt,
        # Extensions for size
        "_size": FHIR_Element,
        # The calculated hash of the data using SHA-1. Represented using base64.
        "hash": FHIR_base64Binary,
        # Extensions for hash
        "_hash": FHIR_Element,
        # A label or set of text to display in place of the data.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The date that the attachment was first created.
        "creation": FHIR_dateTime,
        # Extensions for creation
        "_creation": FHIR_Element,
    },
    total=False,
)
