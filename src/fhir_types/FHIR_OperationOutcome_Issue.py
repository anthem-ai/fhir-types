from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A collection of error, warning, or information messages that result from a system action.
FHIR_OperationOutcome_Issue = TypedDict(
    "FHIR_OperationOutcome_Issue",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates whether the issue indicates a variation from successful processing.
        "severity": Literal["fatal", "error", "warning", "information"],
        # Extensions for severity
        "_severity": FHIR_Element,
        # Describes the type of the issue. The system that creates an OperationOutcome SHALL choose the most applicable code from the IssueType value set, and may additional provide its own code for the error in the details element.
        "code": Literal[
            "invalid",
            "structure",
            "required",
            "value",
            "invariant",
            "security",
            "login",
            "unknown",
            "expired",
            "forbidden",
            "suppressed",
            "processing",
            "not-supported",
            "duplicate",
            "multiple-matches",
            "not-found",
            "deleted",
            "too-long",
            "code-invalid",
            "extension",
            "too-costly",
            "business-rule",
            "conflict",
            "transient",
            "lock-error",
            "no-store",
            "exception",
            "timeout",
            "incomplete",
            "throttled",
            "informational",
        ],
        # Extensions for code
        "_code": FHIR_Element,
        # Additional details about the error. This may be a text description of the error or a system code that identifies the error.
        "details": FHIR_CodeableConcept,
        # Additional diagnostic information about the issue.
        "diagnostics": FHIR_string,
        # Extensions for diagnostics
        "_diagnostics": FHIR_Element,
        # This element is deprecated because it is XML specific. It is replaced by issue.expression, which is format independent, and simpler to parse. For resource issues, this will be a simple XPath limited to element names, repetition indicators and the default child accessor that identifies one of the elements in the resource that caused this issue to be raised.  For HTTP errors, will be "http." + the parameter name.
        "location": List[FHIR_string],
        # Extensions for location
        "_location": List[FHIR_Element],
        # A [simple subset of FHIRPath](fhirpath.html#simple) limited to element names, repetition indicators and the default child accessor that identifies one of the elements in the resource that caused this issue to be raised.
        "expression": List[FHIR_string],
        # Extensions for expression
        "_expression": List[FHIR_Element],
    },
    total=False,
)
