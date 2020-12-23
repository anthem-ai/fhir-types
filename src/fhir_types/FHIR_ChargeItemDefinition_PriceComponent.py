from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_Money import FHIR_Money
from .FHIR_string import FHIR_string

# The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
FHIR_ChargeItemDefinition_PriceComponent = TypedDict(
    "FHIR_ChargeItemDefinition_PriceComponent",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # This code identifies the type of the component.
        "type": FHIR_code,
        # Extensions for type
        "_type": FHIR_Element,
        # A code that identifies the component. Codes may be used to differentiate between kinds of taxes, surcharges, discounts etc.
        "code": FHIR_CodeableConcept,
        # The factor that has been applied on the base price for calculating this component.
        "factor": FHIR_decimal,
        # Extensions for factor
        "_factor": FHIR_Element,
        # The amount calculated for this component.
        "amount": FHIR_Money,
    },
    total=False,
)
