from typing import Any, List, Literal, TypedDict

from .FHIR_Coding import FHIR_Coding
from .FHIR_Reference import FHIR_Reference
from .FHIR_Signature import FHIR_Signature
from .FHIR_string import FHIR_string

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_Signer = TypedDict(
    "FHIR_Contract_Signer",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Role of this Contract signer, e.g. notary, grantee.
        "type": FHIR_Coding,
        # Party which is a signator to this Contract.
        "party": FHIR_Reference,
        # Legally binding Contract DSIG signature contents in Base64.
        "signature": List[FHIR_Signature],
    },
    total=False,
)
