from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.
FHIR_Identifier = TypedDict(
    "FHIR_Identifier",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The purpose of this identifier.
        "use": Literal["usual", "official", "temp", "secondary", "old"],
        # Extensions for use
        "_use": FHIR_Element,
        # A coded type for the identifier that can be used to determine which identifier to use for a specific purpose.
        "type": FHIR_CodeableConcept,
        # Establishes the namespace for the value - that is, a URL that describes a set values that are unique.
        "system": FHIR_uri,
        # Extensions for system
        "_system": FHIR_Element,
        # The portion of the identifier typically relevant to the user and which is unique within the context of the system.
        "value": FHIR_string,
        # Extensions for value
        "_value": FHIR_Element,
        # Time period during which identifier is/was valid for use.
        "period": FHIR_Period,
        # Organization that issued/manages the identifier.
        "assigner": Any,
    },
    total=False,
)
