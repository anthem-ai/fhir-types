from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_PractitionerRole_AvailableTime import FHIR_PractitionerRole_AvailableTime
from .FHIR_PractitionerRole_NotAvailable import FHIR_PractitionerRole_NotAvailable
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.
FHIR_PractitionerRole = TypedDict(
    "FHIR_PractitionerRole",
    {
        # This is a PractitionerRole resource
        "resourceType": Literal["PractitionerRole"],
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
        # Business Identifiers that are specific to a role/location.
        "identifier": List[FHIR_Identifier],
        # Whether this practitioner role record is in active use.
        "active": FHIR_boolean,
        # Extensions for active
        "_active": FHIR_Element,
        # The period during which the person is authorized to act as a practitioner in these role(s) for the organization.
        "period": FHIR_Period,
        # Practitioner that is able to provide the defined services for the organization.
        "practitioner": FHIR_Reference,
        # The organization where the Practitioner performs the roles associated.
        "organization": FHIR_Reference,
        # Roles which this practitioner is authorized to perform for the organization.
        "code": List[FHIR_CodeableConcept],
        # Specific specialty of the practitioner.
        "specialty": List[FHIR_CodeableConcept],
        # The location(s) at which this practitioner provides care.
        "location": List[FHIR_Reference],
        # The list of healthcare services that this worker provides for this role's Organization/Location(s).
        "healthcareService": List[FHIR_Reference],
        # Contact details that are specific to the role/location/service.
        "telecom": List[FHIR_ContactPoint],
        # A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.
        "availableTime": List[FHIR_PractitionerRole_AvailableTime],
        # The practitioner is not available or performing this role during this period of time due to the provided reason.
        "notAvailable": List[FHIR_PractitionerRole_NotAvailable],
        # A description of site availability exceptions, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as details in the available Times and not available Times.
        "availabilityExceptions": FHIR_string,
        # Extensions for availabilityExceptions
        "_availabilityExceptions": FHIR_Element,
        # Technical endpoints providing access to services operated for the practitioner with this role.
        "endpoint": List[FHIR_Reference],
    },
    total=False,
)
