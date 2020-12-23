from typing import Any, List, Literal, TypedDict

from .FHIR_string import FHIR_string
from .FHIR_TestReport_Assert import FHIR_TestReport_Assert
from .FHIR_TestReport_Operation import FHIR_TestReport_Operation

# A summary of information based on the results of executing a TestScript.
FHIR_TestReport_Action1 = TypedDict(
    "FHIR_TestReport_Action1",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An operation would involve a REST request to a server.
        "operation": FHIR_TestReport_Operation,
        # The results of the assertion performed on the previous operations.
        "assert": FHIR_TestReport_Assert,
    },
    total=False,
)
