from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_Signature import FHIR_Signature
from .FHIR_string import FHIR_string

# Describes validation requirements, source(s), status and dates for one or more elements.
FHIR_VerificationResult_Validator = TypedDict(
    "FHIR_VerificationResult_Validator",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Reference to the organization validating information.
        "organization": FHIR_Reference,
        # A digital identity certificate associated with the validator.
        "identityCertificate": FHIR_string,
        # Extensions for identityCertificate
        "_identityCertificate": FHIR_Element,
        # Signed assertion by the validator that they have validated the information.
        "attestationSignature": FHIR_Signature,
    },
    total=False,
)
