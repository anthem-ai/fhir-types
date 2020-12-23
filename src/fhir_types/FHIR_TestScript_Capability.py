from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
FHIR_TestScript_Capability = TypedDict(
    "FHIR_TestScript_Capability",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Whether or not the test execution will require the given capabilities of the server in order for this test script to execute.
        "required": FHIR_boolean,
        # Extensions for required
        "_required": FHIR_Element,
        # Whether or not the test execution will validate the given capabilities of the server in order for this test script to execute.
        "validated": FHIR_boolean,
        # Extensions for validated
        "_validated": FHIR_Element,
        # Description of the capabilities that this test script is requiring the server to support.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Which origin server these requirements apply to.
        "origin": List[FHIR_integer],
        # Extensions for origin
        "_origin": List[FHIR_Element],
        # Which server these requirements apply to.
        "destination": FHIR_integer,
        # Extensions for destination
        "_destination": FHIR_Element,
        # Links to the FHIR specification that describes this interaction and the resources involved in more detail.
        "link": List[FHIR_uri],
        # Extensions for link
        "_link": List[FHIR_Element],
        # Minimum capabilities required of server for test script to execute successfully.   If server does not meet at a minimum the referenced capability statement, then all tests in this script are skipped.
        "capabilities": FHIR_canonical,
    },
    total=False,
)
