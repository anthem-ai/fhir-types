from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string

# A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
FHIR_TestScript_Variable = TypedDict(
    "FHIR_TestScript_Variable",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Descriptive name for this variable.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A default, hard-coded, or user-defined value for this variable.
        "defaultValue": FHIR_string,
        # Extensions for defaultValue
        "_defaultValue": FHIR_Element,
        # A free text natural language description of the variable and its purpose.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The FHIRPath expression to evaluate against the fixture body. When variables are defined, only one of either expression, headerField or path must be specified.
        "expression": FHIR_string,
        # Extensions for expression
        "_expression": FHIR_Element,
        # Will be used to grab the HTTP header field value from the headers that sourceId is pointing to.
        "headerField": FHIR_string,
        # Extensions for headerField
        "_headerField": FHIR_Element,
        # Displayable text string with hint help information to the user when entering a default value.
        "hint": FHIR_string,
        # Extensions for hint
        "_hint": FHIR_Element,
        # XPath or JSONPath to evaluate against the fixture body.  When variables are defined, only one of either expression, headerField or path must be specified.
        "path": FHIR_string,
        # Extensions for path
        "_path": FHIR_Element,
        # Fixture to evaluate the XPath/JSONPath expression or the headerField  against within this variable.
        "sourceId": FHIR_id,
        # Extensions for sourceId
        "_sourceId": FHIR_Element,
    },
    total=False,
)
