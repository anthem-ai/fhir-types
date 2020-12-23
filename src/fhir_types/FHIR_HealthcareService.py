from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_HealthcareService_AvailableTime import FHIR_HealthcareService_AvailableTime
from .FHIR_HealthcareService_Eligibility import FHIR_HealthcareService_Eligibility
from .FHIR_HealthcareService_NotAvailable import FHIR_HealthcareService_NotAvailable
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_markdown import FHIR_markdown
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# The details of a healthcare service available at a location.
FHIR_HealthcareService = TypedDict(
    "FHIR_HealthcareService",
    {
        # This is a HealthcareService resource
        "resourceType": Literal["HealthcareService"],
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
        # External identifiers for this item.
        "identifier": List[FHIR_Identifier],
        # This flag is used to mark the record to not be used. This is not used when a center is closed for maintenance, or for holidays, the notAvailable period is to be used for this.
        "active": FHIR_boolean,
        # Extensions for active
        "_active": FHIR_Element,
        # The organization that provides this healthcare service.
        "providedBy": FHIR_Reference,
        # Identifies the broad category of service being performed or delivered.
        "category": List[FHIR_CodeableConcept],
        # The specific type of service that may be delivered or performed.
        "type": List[FHIR_CodeableConcept],
        # Collection of specialties handled by the service site. This is more of a medical term.
        "specialty": List[FHIR_CodeableConcept],
        # The location(s) where this healthcare service may be provided.
        "location": List[FHIR_Reference],
        # Further description of the service as it would be presented to a consumer while searching.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Any additional description of the service and/or any specific issues not covered by the other attributes, which can be displayed as further detail under the serviceName.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
        # Extra details about the service that can't be placed in the other fields.
        "extraDetails": FHIR_markdown,
        # Extensions for extraDetails
        "_extraDetails": FHIR_Element,
        # If there is a photo/symbol associated with this HealthcareService, it may be included here to facilitate quick identification of the service in a list.
        "photo": FHIR_Attachment,
        # List of contacts related to this specific healthcare service.
        "telecom": List[FHIR_ContactPoint],
        # The location(s) that this service is available to (not where the service is provided).
        "coverageArea": List[FHIR_Reference],
        # The code(s) that detail the conditions under which the healthcare service is available/offered.
        "serviceProvisionCode": List[FHIR_CodeableConcept],
        # Does this service have specific eligibility requirements that need to be met in order to use the service?
        "eligibility": List[FHIR_HealthcareService_Eligibility],
        # Programs that this service is applicable to.
        "program": List[FHIR_CodeableConcept],
        # Collection of characteristics (attributes).
        "characteristic": List[FHIR_CodeableConcept],
        # Some services are specifically made available in multiple languages, this property permits a directory to declare the languages this is offered in. Typically this is only provided where a service operates in communities with mixed languages used.
        "communication": List[FHIR_CodeableConcept],
        # Ways that the service accepts referrals, if this is not provided then it is implied that no referral is required.
        "referralMethod": List[FHIR_CodeableConcept],
        # Indicates whether or not a prospective consumer will require an appointment for a particular service at a site to be provided by the Organization. Indicates if an appointment is required for access to this service.
        "appointmentRequired": FHIR_boolean,
        # Extensions for appointmentRequired
        "_appointmentRequired": FHIR_Element,
        # A collection of times that the Service Site is available.
        "availableTime": List[FHIR_HealthcareService_AvailableTime],
        # The HealthcareService is not available during this period of time due to the provided reason.
        "notAvailable": List[FHIR_HealthcareService_NotAvailable],
        # A description of site availability exceptions, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as details in the available Times and not available Times.
        "availabilityExceptions": FHIR_string,
        # Extensions for availabilityExceptions
        "_availabilityExceptions": FHIR_Element,
        # Technical endpoints providing access to services operated for the specific healthcare services defined at this resource.
        "endpoint": List[FHIR_Reference],
    },
    total=False,
)
