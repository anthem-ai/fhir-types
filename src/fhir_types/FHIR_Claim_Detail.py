from typing import Any, List, Literal, TypedDict

from .FHIR_Claim_SubDetail import FHIR_Claim_SubDetail
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_Money import FHIR_Money
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim_Detail = TypedDict(
    "FHIR_Claim_Detail",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify item entries.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # The type of revenue or cost center providing the product and/or service.
        "revenue": FHIR_CodeableConcept,
        # Code to identify the general type of benefits under which products and services are provided.
        "category": FHIR_CodeableConcept,
        # When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the item.
        "productOrService": FHIR_CodeableConcept,
        # Item typification or modifiers codes to convey additional context for the product or service.
        "modifier": List[FHIR_CodeableConcept],
        # Identifies the program under which this may be recovered.
        "programCode": List[FHIR_CodeableConcept],
        # The number of repetitions of a service or product.
        "quantity": FHIR_Quantity,
        # If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the group.
        "unitPrice": FHIR_Money,
        # A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amount.
        "factor": FHIR_decimal,
        # Extensions for factor
        "_factor": FHIR_Element,
        # The quantity times the unit price for an additional service or product or charge.
        "net": FHIR_Money,
        # Unique Device Identifiers associated with this line item.
        "udi": List[FHIR_Reference],
        # A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.
        "subDetail": List[FHIR_Claim_SubDetail],
    },
    total=False,
)
