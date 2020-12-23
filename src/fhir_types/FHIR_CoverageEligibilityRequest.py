from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_CoverageEligibilityRequest_Insurance import (
    FHIR_CoverageEligibilityRequest_Insurance,
)
from .FHIR_CoverageEligibilityRequest_Item import FHIR_CoverageEligibilityRequest_Item
from .FHIR_CoverageEligibilityRequest_SupportingInfo import (
    FHIR_CoverageEligibilityRequest_SupportingInfo,
)
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
FHIR_CoverageEligibilityRequest = TypedDict(
    "FHIR_CoverageEligibilityRequest",
    {
        # This is a CoverageEligibilityRequest resource
        "resourceType": Literal["CoverageEligibilityRequest"],
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
        # A unique identifier assigned to this coverage eligiblity request.
        "identifier": List[FHIR_Identifier],
        # The status of the resource instance.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # When the requestor expects the processor to complete processing.
        "priority": FHIR_CodeableConcept,
        # Code to specify whether requesting: prior authorization requirements for some service categories or billing codes; benefits for coverages specified or discovered; discovery and return of coverages for the patient; and/or validation that the specified coverage is in-force at the date/period specified or 'now' if not specified.
        "purpose": List[
            Literal["auth-requirements", "benefits", "discovery", "validation"]
        ],
        # Extensions for purpose
        "_purpose": List[FHIR_Element],
        # The party who is the beneficiary of the supplied coverage and for whom eligibility is sought.
        "patient": FHIR_Reference,
        # The date or dates when the enclosed suite of services were performed or completed.
        "servicedDate": str,
        # Extensions for servicedDate
        "_servicedDate": FHIR_Element,
        # The date or dates when the enclosed suite of services were performed or completed.
        "servicedPeriod": FHIR_Period,
        # The date when this resource was created.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # Person who created the request.
        "enterer": FHIR_Reference,
        # The provider which is responsible for the request.
        "provider": FHIR_Reference,
        # The Insurer who issued the coverage in question and is the recipient of the request.
        "insurer": FHIR_Reference,
        # Facility where the services are intended to be provided.
        "facility": FHIR_Reference,
        # Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.
        "supportingInfo": List[FHIR_CoverageEligibilityRequest_SupportingInfo],
        # Financial instruments for reimbursement for the health care products and services.
        "insurance": List[FHIR_CoverageEligibilityRequest_Insurance],
        # Service categories or billable services for which benefit details and/or an authorization prior to service delivery may be required by the payor.
        "item": List[FHIR_CoverageEligibilityRequest_Item],
    },
    total=False,
)
