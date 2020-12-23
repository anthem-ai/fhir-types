from typing import Any, List, Literal, TypedDict

from .FHIR_CapabilityStatement_Endpoint import FHIR_CapabilityStatement_Endpoint
from .FHIR_CapabilityStatement_SupportedMessage import (
    FHIR_CapabilityStatement_SupportedMessage,
)
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
FHIR_CapabilityStatement_Messaging = TypedDict(
    "FHIR_CapabilityStatement_Messaging",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An endpoint (network accessible address) to which messages and/or replies are to be sent.
        "endpoint": List[FHIR_CapabilityStatement_Endpoint],
        # Length if the receiver's reliable messaging cache in minutes (if a receiver) or how long the cache length on the receiver should be (if a sender).
        "reliableCache": FHIR_unsignedInt,
        # Extensions for reliableCache
        "_reliableCache": FHIR_Element,
        # Documentation about the system's messaging capabilities for this endpoint not otherwise documented by the capability statement.  For example, the process for becoming an authorized messaging exchange partner.
        "documentation": FHIR_markdown,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # References to message definitions for messages this system can send or receive.
        "supportedMessage": List[FHIR_CapabilityStatement_SupportedMessage],
    },
    total=False,
)
