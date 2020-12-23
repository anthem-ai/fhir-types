from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.
FHIR_MessageDefinition_AllowedResponse = TypedDict(
    "FHIR_MessageDefinition_AllowedResponse",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A reference to the message definition that must be adhered to by this supported response.
        "message": FHIR_canonical,
        # Provides a description of the circumstances in which this response should be used (as opposed to one of the alternative responses).
        "situation": FHIR_markdown,
        # Extensions for situation
        "_situation": FHIR_Element,
    },
    total=False,
)
