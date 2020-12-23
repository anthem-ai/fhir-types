from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string

# A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
FHIR_TestScript_Assert = TypedDict(
    "FHIR_TestScript_Assert",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The label would be used for tracking/logging purposes by test engines.
        "label": FHIR_string,
        # Extensions for label
        "_label": FHIR_Element,
        # The description would be used by test engines for tracking and reporting purposes.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The direction to use for the assertion.
        "direction": Literal["response", "request"],
        # Extensions for direction
        "_direction": FHIR_Element,
        # Id of the source fixture used as the contents to be evaluated by either the "source/expression" or "sourceId/path" definition.
        "compareToSourceId": FHIR_string,
        # Extensions for compareToSourceId
        "_compareToSourceId": FHIR_Element,
        # The FHIRPath expression to evaluate against the source fixture. When compareToSourceId is defined, either compareToSourceExpression or compareToSourcePath must be defined, but not both.
        "compareToSourceExpression": FHIR_string,
        # Extensions for compareToSourceExpression
        "_compareToSourceExpression": FHIR_Element,
        # XPath or JSONPath expression to evaluate against the source fixture. When compareToSourceId is defined, either compareToSourceExpression or compareToSourcePath must be defined, but not both.
        "compareToSourcePath": FHIR_string,
        # Extensions for compareToSourcePath
        "_compareToSourcePath": FHIR_Element,
        # The mime-type contents to compare against the request or response message 'Content-Type' header.
        "contentType": FHIR_code,
        # Extensions for contentType
        "_contentType": FHIR_Element,
        # The FHIRPath expression to be evaluated against the request or response message contents - HTTP headers and payload.
        "expression": FHIR_string,
        # Extensions for expression
        "_expression": FHIR_Element,
        # The HTTP header field name e.g. 'Location'.
        "headerField": FHIR_string,
        # Extensions for headerField
        "_headerField": FHIR_Element,
        # The ID of a fixture.  Asserts that the response contains at a minimum the fixture specified by minimumId.
        "minimumId": FHIR_string,
        # Extensions for minimumId
        "_minimumId": FHIR_Element,
        # Whether or not the test execution performs validation on the bundle navigation links.
        "navigationLinks": FHIR_boolean,
        # Extensions for navigationLinks
        "_navigationLinks": FHIR_Element,
        # The operator type defines the conditional behavior of the assert. If not defined, the default is equals.
        "operator": Literal[
            "equals",
            "notEquals",
            "in",
            "notIn",
            "greaterThan",
            "lessThan",
            "empty",
            "notEmpty",
            "contains",
            "notContains",
            "eval",
        ],
        # Extensions for operator
        "_operator": FHIR_Element,
        # The XPath or JSONPath expression to be evaluated against the fixture representing the response received from server.
        "path": FHIR_string,
        # Extensions for path
        "_path": FHIR_Element,
        # The request method or HTTP operation code to compare against that used by the client system under test.
        "requestMethod": Literal[
            "delete", "get", "options", "patch", "post", "put", "head"
        ],
        # Extensions for requestMethod
        "_requestMethod": FHIR_Element,
        # The value to use in a comparison against the request URL path string.
        "requestURL": FHIR_string,
        # Extensions for requestURL
        "_requestURL": FHIR_Element,
        # The type of the resource.  See http://build.fhir.org/resourcelist.html.
        "resource": FHIR_code,
        # Extensions for resource
        "_resource": FHIR_Element,
        # okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable.
        "response": Literal[
            "okay",
            "created",
            "noContent",
            "notModified",
            "bad",
            "forbidden",
            "notFound",
            "methodNotAllowed",
            "conflict",
            "gone",
            "preconditionFailed",
            "unprocessable",
        ],
        # Extensions for response
        "_response": FHIR_Element,
        # The value of the HTTP response code to be tested.
        "responseCode": FHIR_string,
        # Extensions for responseCode
        "_responseCode": FHIR_Element,
        # Fixture to evaluate the XPath/JSONPath expression or the headerField  against.
        "sourceId": FHIR_id,
        # Extensions for sourceId
        "_sourceId": FHIR_Element,
        # The ID of the Profile to validate against.
        "validateProfileId": FHIR_id,
        # Extensions for validateProfileId
        "_validateProfileId": FHIR_Element,
        # The value to compare to.
        "value": FHIR_string,
        # Extensions for value
        "_value": FHIR_Element,
        # Whether or not the test execution will produce a warning only on error for this assert.
        "warningOnly": FHIR_boolean,
        # Extensions for warningOnly
        "_warningOnly": FHIR_Element,
    },
    total=False,
)
