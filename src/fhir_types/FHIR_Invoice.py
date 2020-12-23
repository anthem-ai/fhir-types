from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Invoice_LineItem import FHIR_Invoice_LineItem
from .FHIR_Invoice_Participant import FHIR_Invoice_Participant
from .FHIR_Invoice_PriceComponent import FHIR_Invoice_PriceComponent
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Money import FHIR_Money
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
FHIR_Invoice = TypedDict(
    "FHIR_Invoice",
    {
        # This is a Invoice resource
        "resourceType": Literal["Invoice"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifier of this Invoice, often used for reference in correspondence about this invoice or for tracking of payments.
        "identifier": List[FHIR_Identifier],
        # The current state of the Invoice.
        "status": Literal[
            "draft", "issued", "balanced", "cancelled", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # In case of Invoice cancellation a reason must be given (entered in error, superseded by corrected invoice etc.).
        "cancelledReason": FHIR_string,
        # Extensions for cancelledReason
        "_cancelledReason": FHIR_Element,
        # Type of Invoice depending on domain, realm an usage (e.g. internal/external, dental, preliminary).
        "type": FHIR_CodeableConcept,
        # The individual or set of individuals receiving the goods and services billed in this invoice.
        "subject": FHIR_Reference,
        # The individual or Organization responsible for balancing of this invoice.
        "recipient": FHIR_Reference,
        # Date/time(s) of when this Invoice was posted.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Indicates who or what performed or participated in the charged service.
        "participant": List[FHIR_Invoice_Participant],
        # The organizationissuing the Invoice.
        "issuer": FHIR_Reference,
        # Account which is supposed to be balanced with this Invoice.
        "account": FHIR_Reference,
        # Each line item represents one charge for goods and services rendered. Details such as date, code and amount are found in the referenced ChargeItem resource.
        "lineItem": List[FHIR_Invoice_LineItem],
        # The total amount for the Invoice may be calculated as the sum of the line items with surcharges/deductions that apply in certain conditions.  The priceComponent element can be used to offer transparency to the recipient of the Invoice of how the total price was calculated.
        "totalPriceComponent": List[FHIR_Invoice_PriceComponent],
        # Invoice total , taxes excluded.
        "totalNet": FHIR_Money,
        # Invoice total, tax included.
        "totalGross": FHIR_Money,
        # Payment details such as banking details, period of payment, deductibles, methods of payment.
        "paymentTerms": FHIR_markdown,
        # Extensions for paymentTerms
        "_paymentTerms": FHIR_Element,
        # Comments made about the invoice by the issuer, subject, or other participants.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
