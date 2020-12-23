from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.
FHIR_Expression = TypedDict(
    "FHIR_Expression",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # A brief, natural language description of the condition that effectively communicates the intended semantics.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # A short name assigned to the expression to allow for multiple reuse of the expression in the context where it is defined.
        "name": FHIR_id,
        # Extensions for name
        "_name": FHIR_Element,
        # The media type of the language for the expression.
        "language": Literal["text/cql", "text/fhirpath", "application/x-fhir-query"],
        # Extensions for language
        "_language": FHIR_Element,
        # An expression in the specified language that returns a value.
        "expression": FHIR_string,
        # Extensions for expression
        "_expression": FHIR_Element,
        # A URI that defines where the expression is found.
        "reference": FHIR_uri,
        # Extensions for reference
        "_reference": FHIR_Element,
    },
    total=False,
)
