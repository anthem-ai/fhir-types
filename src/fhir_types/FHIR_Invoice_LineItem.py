from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Invoice_PriceComponent import FHIR_Invoice_PriceComponent
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
FHIR_Invoice_LineItem = TypedDict(
    "FHIR_Invoice_LineItem",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Sequence in which the items appear on the invoice.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # The ChargeItem contains information such as the billing code, date, amount etc. If no further details are required for the lineItem, inline billing codes can be added using the CodeableConcept data type instead of the Reference.
        "chargeItemReference": FHIR_Reference,
        # The ChargeItem contains information such as the billing code, date, amount etc. If no further details are required for the lineItem, inline billing codes can be added using the CodeableConcept data type instead of the Reference.
        "chargeItemCodeableConcept": FHIR_CodeableConcept,
        # The price for a ChargeItem may be calculated as a base price with surcharges/deductions that apply in certain conditions. A ChargeItemDefinition resource that defines the prices, factors and conditions that apply to a billing code is currently under development. The priceComponent element can be used to offer transparency to the recipient of the Invoice as to how the prices have been calculated.
        "priceComponent": List[FHIR_Invoice_PriceComponent],
    },
    total=False,
)
