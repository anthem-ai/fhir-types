from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Money import FHIR_Money
from .FHIR_string import FHIR_string

# This resource provides the adjudication details from the processing of a Claim resource.
FHIR_ClaimResponse_Payment = TypedDict(
    "FHIR_ClaimResponse_Payment",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Whether this represents partial or complete payment of the benefits payable.
        "type": FHIR_CodeableConcept,
        # Total amount of all adjustments to this payment included in this transaction which are not related to this claim's adjudication.
        "adjustment": FHIR_Money,
        # Reason for the payment adjustment.
        "adjustmentReason": FHIR_CodeableConcept,
        # Estimated date the payment will be issued or the actual issue date of payment.
        "date": FHIR_date,
        # Extensions for date
        "_date": FHIR_Element,
        # Benefits payable less any payment adjustment.
        "amount": FHIR_Money,
        # Issuer's unique identifier for the payment instrument.
        "identifier": FHIR_Identifier,
    },
    total=False,
)
