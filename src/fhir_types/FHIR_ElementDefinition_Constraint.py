from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string

# Captures constraints on each element within the resource, profile, or extension.
FHIR_ElementDefinition_Constraint = TypedDict(
    "FHIR_ElementDefinition_Constraint",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Allows identification of which elements have their cardinalities impacted by the constraint.  Will not be referenced for constraints that do not affect cardinality.
        "key": FHIR_id,
        # Extensions for key
        "_key": FHIR_Element,
        # Description of why this constraint is necessary or appropriate.
        "requirements": FHIR_string,
        # Extensions for requirements
        "_requirements": FHIR_Element,
        # Identifies the impact constraint violation has on the conformance of the instance.
        "severity": Literal["error", "warning"],
        # Extensions for severity
        "_severity": FHIR_Element,
        # Text that can be used to describe the constraint in messages identifying that the constraint has been violated.
        "human": FHIR_string,
        # Extensions for human
        "_human": FHIR_Element,
        # A [FHIRPath](fhirpath.html) expression of constraint that can be executed to see if this constraint is met.
        "expression": FHIR_string,
        # Extensions for expression
        "_expression": FHIR_Element,
        # An XPath expression of constraint that can be executed to see if this constraint is met.
        "xpath": FHIR_string,
        # Extensions for xpath
        "_xpath": FHIR_Element,
        # A reference to the original source of the constraint, for traceability purposes.
        "source": FHIR_canonical,
    },
    total=False,
)
