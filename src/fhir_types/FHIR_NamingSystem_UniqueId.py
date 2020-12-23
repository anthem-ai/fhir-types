from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string

# A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
FHIR_NamingSystem_UniqueId = TypedDict(
    "FHIR_NamingSystem_UniqueId",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifies the unique identifier scheme used for this particular identifier.
        "type": Literal["oid", "uuid", "uri", "other"],
        # Extensions for type
        "_type": FHIR_Element,
        # The string that should be sent over the wire to identify the code system or identifier system.
        "value": FHIR_string,
        # Extensions for value
        "_value": FHIR_Element,
        # Indicates whether this identifier is the "preferred" identifier of this type.
        "preferred": FHIR_boolean,
        # Extensions for preferred
        "_preferred": FHIR_Element,
        # Notes about the past or intended usage of this identifier.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
        # Identifies the period of time over which this identifier is considered appropriate to refer to the naming system.  Outside of this window, the identifier might be non-deterministic.
        "period": FHIR_Period,
    },
    total=False,
)
