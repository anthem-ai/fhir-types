from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Location_HoursOfOperation import FHIR_Location_HoursOfOperation
from .FHIR_Location_Position import FHIR_Location_Position
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
FHIR_Location = TypedDict(
    "FHIR_Location",
    {
        # This is a Location resource
        "resourceType": Literal["Location"],
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
        # Unique code or number identifying the location to its users.
        "identifier": List[FHIR_Identifier],
        # The status property covers the general availability of the resource, not the current value which may be covered by the operationStatus, or by a schedule/slots if they are configured for the location.
        "status": Literal["active", "suspended", "inactive"],
        # Extensions for status
        "_status": FHIR_Element,
        # The operational status covers operation values most relevant to beds (but can also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis chair). This typically covers concepts such as contamination, housekeeping, and other activities like maintenance.
        "operationalStatus": FHIR_Coding,
        # Name of the location as used by humans. Does not need to be unique.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A list of alternate names that the location is known as, or was known as, in the past.
        "alias": List[FHIR_string],
        # Extensions for alias
        "_alias": List[FHIR_Element],
        # Description of the Location, which helps in finding or referencing the place.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Indicates whether a resource instance represents a specific location or a class of locations.
        "mode": Literal["instance", "kind"],
        # Extensions for mode
        "_mode": FHIR_Element,
        # Indicates the type of function performed at the location.
        "type": List[FHIR_CodeableConcept],
        # The contact details of communication devices available at the location. This can include phone numbers, fax numbers, mobile numbers, email addresses and web sites.
        "telecom": List[FHIR_ContactPoint],
        # Physical location.
        "address": FHIR_Address,
        # Physical form of the location, e.g. building, room, vehicle, road.
        "physicalType": FHIR_CodeableConcept,
        # The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).
        "position": FHIR_Location_Position,
        # The organization responsible for the provisioning and upkeep of the location.
        "managingOrganization": FHIR_Reference,
        # Another Location of which this Location is physically a part of.
        "partOf": FHIR_Reference,
        # What days/times during a week is this location usually open.
        "hoursOfOperation": List[FHIR_Location_HoursOfOperation],
        # A description of when the locations opening ours are different to normal, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as detailed in the opening hours Times.
        "availabilityExceptions": FHIR_string,
        # Extensions for availabilityExceptions
        "_availabilityExceptions": FHIR_Element,
        # Technical endpoints providing access to services operated for the location.
        "endpoint": List[FHIR_Reference],
    },
    total=False,
)
