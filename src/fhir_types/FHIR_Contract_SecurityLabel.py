from typing import Any, List, Literal, TypedDict

from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_SecurityLabel = TypedDict(
    "FHIR_Contract_SecurityLabel",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Number used to link this term or term element to the applicable Security Label.
        "number": List[FHIR_unsignedInt],
        # Extensions for number
        "_number": List[FHIR_Element],
        # Security label privacy tag that species the level of confidentiality protection required for this term and/or term elements.
        "classification": FHIR_Coding,
        # Security label privacy tag that species the applicable privacy and security policies governing this term and/or term elements.
        "category": List[FHIR_Coding],
        # Security label privacy tag that species the manner in which term and/or term elements are to be protected.
        "control": List[FHIR_Coding],
    },
    total=False,
)
