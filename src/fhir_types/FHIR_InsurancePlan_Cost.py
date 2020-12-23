from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# Details of a Health Insurance product/plan provided by an organization.
FHIR_InsurancePlan_Cost = TypedDict(
    "FHIR_InsurancePlan_Cost",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Type of cost (copay; individual cap; family cap; coinsurance; deductible).
        "type": FHIR_CodeableConcept,
        # Whether the cost applies to in-network or out-of-network providers (in-network; out-of-network; other).
        "applicability": FHIR_CodeableConcept,
        # Additional information about the cost, such as information about funding sources (e.g. HSA, HRA, FSA, RRA).
        "qualifiers": List[FHIR_CodeableConcept],
        # The actual cost value. (some of the costs may be represented as percentages rather than currency, e.g. 10% coinsurance).
        "value": FHIR_Quantity,
    },
    total=False,
)
