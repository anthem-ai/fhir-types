from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.
FHIR_MessageDefinition_Focus = TypedDict(
    "FHIR_MessageDefinition_Focus",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The kind of resource that must be the focus for this message.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # A profile that reflects constraints for the focal resource (and potentially for related resources).
        "profile": FHIR_canonical,
        # Identifies the minimum number of resources of this type that must be pointed to by a message in order for it to be valid against this MessageDefinition.
        "min": FHIR_unsignedInt,
        # Extensions for min
        "_min": FHIR_Element,
        # Identifies the maximum number of resources of this type that must be pointed to by a message in order for it to be valid against this MessageDefinition.
        "max": FHIR_string,
        # Extensions for max
        "_max": FHIR_Element,
    },
    total=False,
)
