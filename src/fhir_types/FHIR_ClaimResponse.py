from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_ClaimResponse_AddItem import FHIR_ClaimResponse_AddItem
from .FHIR_ClaimResponse_Adjudication import FHIR_ClaimResponse_Adjudication
from .FHIR_ClaimResponse_Error import FHIR_ClaimResponse_Error
from .FHIR_ClaimResponse_Insurance import FHIR_ClaimResponse_Insurance
from .FHIR_ClaimResponse_Item import FHIR_ClaimResponse_Item
from .FHIR_ClaimResponse_Payment import FHIR_ClaimResponse_Payment
from .FHIR_ClaimResponse_ProcessNote import FHIR_ClaimResponse_ProcessNote
from .FHIR_ClaimResponse_Total import FHIR_ClaimResponse_Total
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# This resource provides the adjudication details from the processing of a Claim resource.
FHIR_ClaimResponse = TypedDict(
    "FHIR_ClaimResponse",
    {
        # This is a ClaimResponse resource
        "resourceType": Literal["ClaimResponse"],
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
        # A unique identifier assigned to this claim response.
        "identifier": List[FHIR_Identifier],
        # The status of the resource instance.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service.
        "type": FHIR_CodeableConcept,
        # A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service.
        "subType": FHIR_CodeableConcept,
        # A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the future.
        "use": FHIR_code,
        # Extensions for use
        "_use": FHIR_Element,
        # The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for facast reimbursement is sought.
        "patient": FHIR_Reference,
        # The date this resource was created.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # The party responsible for authorization, adjudication and reimbursement.
        "insurer": FHIR_Reference,
        # The provider which is responsible for the claim, predetermination or preauthorization.
        "requestor": FHIR_Reference,
        # Original request resource reference.
        "request": FHIR_Reference,
        # The outcome of the claim, predetermination, or preauthorization processing.
        "outcome": FHIR_code,
        # Extensions for outcome
        "_outcome": FHIR_Element,
        # A human readable description of the status of the adjudication.
        "disposition": FHIR_string,
        # Extensions for disposition
        "_disposition": FHIR_Element,
        # Reference from the Insurer which is used in later communications which refers to this adjudication.
        "preAuthRef": FHIR_string,
        # Extensions for preAuthRef
        "_preAuthRef": FHIR_Element,
        # The time frame during which this authorization is effective.
        "preAuthPeriod": FHIR_Period,
        # Type of Party to be reimbursed: subscriber, provider, other.
        "payeeType": FHIR_CodeableConcept,
        # A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.
        "item": List[FHIR_ClaimResponse_Item],
        # The first-tier service adjudications for payor added product or service lines.
        "addItem": List[FHIR_ClaimResponse_AddItem],
        # The adjudication results which are presented at the header level rather than at the line-item or add-item levels.
        "adjudication": List[FHIR_ClaimResponse_Adjudication],
        # Categorized monetary totals for the adjudication.
        "total": List[FHIR_ClaimResponse_Total],
        # Payment details for the adjudication of the claim.
        "payment": FHIR_ClaimResponse_Payment,
        # A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whom.
        "fundsReserve": FHIR_CodeableConcept,
        # A code for the form to be used for printing the content.
        "formCode": FHIR_CodeableConcept,
        # The actual form, by reference or inclusion, for printing the content or an EOB.
        "form": FHIR_Attachment,
        # A note that describes or explains adjudication results in a human readable form.
        "processNote": List[FHIR_ClaimResponse_ProcessNote],
        # Request for additional supporting or authorizing information.
        "communicationRequest": List[FHIR_Reference],
        # Financial instruments for reimbursement for the health care products and services specified on the claim.
        "insurance": List[FHIR_ClaimResponse_Insurance],
        # Errors encountered during the processing of the adjudication.
        "error": List[FHIR_ClaimResponse_Error],
    },
    total=False,
)
