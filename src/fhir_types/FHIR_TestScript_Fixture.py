from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
FHIR_TestScript_Fixture = TypedDict(
    "FHIR_TestScript_Fixture",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Whether or not to implicitly create the fixture during setup. If true, the fixture is automatically created on each server being tested during setup, therefore no create operation is required for this fixture in the TestScript.setup section.
        "autocreate": FHIR_boolean,
        # Extensions for autocreate
        "_autocreate": FHIR_Element,
        # Whether or not to implicitly delete the fixture during teardown. If true, the fixture is automatically deleted on each server being tested during teardown, therefore no delete operation is required for this fixture in the TestScript.teardown section.
        "autodelete": FHIR_boolean,
        # Extensions for autodelete
        "_autodelete": FHIR_Element,
        # Reference to the resource (containing the contents of the resource needed for operations).
        "resource": FHIR_Reference,
    },
    total=False,
)
