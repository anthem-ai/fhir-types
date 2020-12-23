from typing import Any, List, Literal, TypedDict

from .FHIR_Claim_Accident import FHIR_Claim_Accident
from .FHIR_Claim_CareTeam import FHIR_Claim_CareTeam
from .FHIR_Claim_Diagnosis import FHIR_Claim_Diagnosis
from .FHIR_Claim_Insurance import FHIR_Claim_Insurance
from .FHIR_Claim_Item import FHIR_Claim_Item
from .FHIR_Claim_Payee import FHIR_Claim_Payee
from .FHIR_Claim_Procedure import FHIR_Claim_Procedure
from .FHIR_Claim_Related import FHIR_Claim_Related
from .FHIR_Claim_SupportingInfo import FHIR_Claim_SupportingInfo
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Money import FHIR_Money
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim = TypedDict(
    "FHIR_Claim",
    {
        # This is a Claim resource
        "resourceType": Literal["Claim"],
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
        # A unique identifier assigned to this claim.
        "identifier": List[FHIR_Identifier],
        # The status of the resource instance.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # The category of claim, e.g. oral, pharmacy, vision, institutional, professional.
        "type": FHIR_CodeableConcept,
        # A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service.
        "subType": FHIR_CodeableConcept,
        # A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the future.
        "use": Literal["claim", "preauthorization", "predetermination"],
        # Extensions for use
        "_use": FHIR_Element,
        # The party to whom the professional services and/or products have been supplied or are being considered and for whom actual or forecast reimbursement is sought.
        "patient": FHIR_Reference,
        # The period for which charges are being submitted.
        "billablePeriod": FHIR_Period,
        # The date this resource was created.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # Individual who created the claim, predetermination or preauthorization.
        "enterer": FHIR_Reference,
        # The Insurer who is target of the request.
        "insurer": FHIR_Reference,
        # The provider which is responsible for the claim, predetermination or preauthorization.
        "provider": FHIR_Reference,
        # The provider-required urgency of processing the request. Typical values include: stat, routine deferred.
        "priority": FHIR_CodeableConcept,
        # A code to indicate whether and for whom funds are to be reserved for future claims.
        "fundsReserve": FHIR_CodeableConcept,
        # Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.
        "related": List[FHIR_Claim_Related],
        # Prescription to support the dispensing of pharmacy, device or vision products.
        "prescription": FHIR_Reference,
        # Original prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or products.
        "originalPrescription": FHIR_Reference,
        # The party to be reimbursed for cost of the products and services according to the terms of the policy.
        "payee": FHIR_Claim_Payee,
        # A reference to a referral resource.
        "referral": FHIR_Reference,
        # Facility where the services were provided.
        "facility": FHIR_Reference,
        # The members of the team who provided the products and services.
        "careTeam": List[FHIR_Claim_CareTeam],
        # Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.
        "supportingInfo": List[FHIR_Claim_SupportingInfo],
        # Information about diagnoses relevant to the claim items.
        "diagnosis": List[FHIR_Claim_Diagnosis],
        # Procedures performed on the patient relevant to the billing items with the claim.
        "procedure": List[FHIR_Claim_Procedure],
        # Financial instruments for reimbursement for the health care products and services specified on the claim.
        "insurance": List[FHIR_Claim_Insurance],
        # Details of an accident which resulted in injuries which required the products and services listed in the claim.
        "accident": FHIR_Claim_Accident,
        # A claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-details.
        "item": List[FHIR_Claim_Item],
        # The total value of the all the items in the claim.
        "total": FHIR_Money,
    },
    total=False,
)
