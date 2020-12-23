from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A slot of time on a schedule that may be available for booking appointments.
FHIR_Slot = TypedDict(
    "FHIR_Slot",
    {
        # This is a Slot resource
        "resourceType": Literal["Slot"],
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
        # External Ids for this item.
        "identifier": List[FHIR_Identifier],
        # A broad categorization of the service that is to be performed during this appointment.
        "serviceCategory": List[FHIR_CodeableConcept],
        # The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource.
        "serviceType": List[FHIR_CodeableConcept],
        # The specialty of a practitioner that would be required to perform the service requested in this appointment.
        "specialty": List[FHIR_CodeableConcept],
        # The style of appointment or patient that may be booked in the slot (not service type).
        "appointmentType": FHIR_CodeableConcept,
        # The schedule resource that this slot defines an interval of status information.
        "schedule": FHIR_Reference,
        # busy | free | busy-unavailable | busy-tentative | entered-in-error.
        "status": Literal[
            "busy", "free", "busy-unavailable", "busy-tentative", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # Date/Time that the slot is to begin.
        "start": FHIR_instant,
        # Extensions for start
        "_start": FHIR_Element,
        # Date/Time that the slot is to conclude.
        "end": FHIR_instant,
        # Extensions for end
        "_end": FHIR_Element,
        # This slot has already been overbooked, appointments are unlikely to be accepted for this time.
        "overbooked": FHIR_boolean,
        # Extensions for overbooked
        "_overbooked": FHIR_Element,
        # Comments on the slot to describe any extended information. Such as custom constraints on the slot.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
    },
    total=False,
)
