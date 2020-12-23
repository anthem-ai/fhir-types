from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_integer import FHIR_integer
from .FHIR_string import FHIR_string
from .FHIR_TestScript_RequestHeader import FHIR_TestScript_RequestHeader

# A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
FHIR_TestScript_Operation = TypedDict(
    "FHIR_TestScript_Operation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Server interaction or operation type.
        "type": FHIR_Coding,
        # The type of the resource.  See http://build.fhir.org/resourcelist.html.
        "resource": FHIR_code,
        # Extensions for resource
        "_resource": FHIR_Element,
        # The label would be used for tracking/logging purposes by test engines.
        "label": FHIR_string,
        # Extensions for label
        "_label": FHIR_Element,
        # The description would be used by test engines for tracking and reporting purposes.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The mime-type to use for RESTful operation in the 'Accept' header.
        "accept": FHIR_code,
        # Extensions for accept
        "_accept": FHIR_Element,
        # The mime-type to use for RESTful operation in the 'Content-Type' header.
        "contentType": FHIR_code,
        # Extensions for contentType
        "_contentType": FHIR_Element,
        # The server where the request message is destined for.  Must be one of the server numbers listed in TestScript.destination section.
        "destination": FHIR_integer,
        # Extensions for destination
        "_destination": FHIR_Element,
        # Whether or not to implicitly send the request url in encoded format. The default is true to match the standard RESTful client behavior. Set to false when communicating with a server that does not support encoded url paths.
        "encodeRequestUrl": FHIR_boolean,
        # Extensions for encodeRequestUrl
        "_encodeRequestUrl": FHIR_Element,
        # The HTTP method the test engine MUST use for this operation regardless of any other operation details.
        "method": Literal["delete", "get", "options", "patch", "post", "put", "head"],
        # Extensions for method
        "_method": FHIR_Element,
        # The server where the request message originates from.  Must be one of the server numbers listed in TestScript.origin section.
        "origin": FHIR_integer,
        # Extensions for origin
        "_origin": FHIR_Element,
        # Path plus parameters after [type].  Used to set parts of the request URL explicitly.
        "params": FHIR_string,
        # Extensions for params
        "_params": FHIR_Element,
        # Header elements would be used to set HTTP headers.
        "requestHeader": List[FHIR_TestScript_RequestHeader],
        # The fixture id (maybe new) to map to the request.
        "requestId": FHIR_id,
        # Extensions for requestId
        "_requestId": FHIR_Element,
        # The fixture id (maybe new) to map to the response.
        "responseId": FHIR_id,
        # Extensions for responseId
        "_responseId": FHIR_Element,
        # The id of the fixture used as the body of a PUT or POST request.
        "sourceId": FHIR_id,
        # Extensions for sourceId
        "_sourceId": FHIR_Element,
        # Id of fixture used for extracting the [id],  [type], and [vid] for GET requests.
        "targetId": FHIR_id,
        # Extensions for targetId
        "_targetId": FHIR_Element,
        # Complete request URL.
        "url": FHIR_string,
        # Extensions for url
        "_url": FHIR_Element,
    },
    total=False,
)
