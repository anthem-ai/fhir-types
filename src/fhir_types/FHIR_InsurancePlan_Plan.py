from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_InsurancePlan_GeneralCost import FHIR_InsurancePlan_GeneralCost
from .FHIR_InsurancePlan_SpecificCost import FHIR_InsurancePlan_SpecificCost
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Details of a Health Insurance product/plan provided by an organization.
FHIR_InsurancePlan_Plan = TypedDict(
    "FHIR_InsurancePlan_Plan",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Business identifiers assigned to this health insurance plan which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # Type of plan. For example, "Platinum" or "High Deductable".
        "type": FHIR_CodeableConcept,
        # The geographic region in which a health insurance plan's benefits apply.
        "coverageArea": List[FHIR_Reference],
        # Reference to the network that providing the type of coverage.
        "network": List[FHIR_Reference],
        # Overall costs associated with the plan.
        "generalCost": List[FHIR_InsurancePlan_GeneralCost],
        # Costs associated with the coverage provided by the product.
        "specificCost": List[FHIR_InsurancePlan_SpecificCost],
    },
    total=False,
)
