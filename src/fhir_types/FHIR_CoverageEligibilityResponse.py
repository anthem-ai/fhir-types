from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_CoverageEligibilityResponse_Error import (
    FHIR_CoverageEligibilityResponse_Error,
)
from .FHIR_CoverageEligibilityResponse_Insurance import (
    FHIR_CoverageEligibilityResponse_Insurance,
)
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

# This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
FHIR_CoverageEligibilityResponse = TypedDict(
    "FHIR_CoverageEligibilityResponse",
    {
        # This is a CoverageEligibilityResponse resource
        "resourceType": Literal["CoverageEligibilityResponse"],
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
        # The date this resource was created.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # The provider which is responsible for the request.
        "requestor": FHIR_Reference,
        # Reference to the original request resource.
        "request": FHIR_Reference,
        # The outcome of the request processing.
        "outcome": Literal["queued", "complete", "error", "partial"],
        # Extensions for outcome
        "_outcome": FHIR_Element,
        # A human readable description of the status of the adjudication.
        "disposition": FHIR_string,
        # Extensions for disposition
        "_disposition": FHIR_Element,
        # The Insurer who issued the coverage in question and is the author of the response.
        "insurer": FHIR_Reference,
        # Financial instruments for reimbursement for the health care products and services.
        "insurance": List[FHIR_CoverageEligibilityResponse_Insurance],
        # A reference from the Insurer to which these services pertain to be used on further communication and as proof that the request occurred.
        "preAuthRef": FHIR_string,
        # Extensions for preAuthRef
        "_preAuthRef": FHIR_Element,
        # A code for the form to be used for printing the content.
        "form": FHIR_CodeableConcept,
        # Errors encountered during the processing of the request.
        "error": List[FHIR_CoverageEligibilityResponse_Error],
    },
    total=False,
)
