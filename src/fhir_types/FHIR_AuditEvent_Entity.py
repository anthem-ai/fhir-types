from typing import Any, List, Literal, TypedDict

from .FHIR_AuditEvent_Detail import FHIR_AuditEvent_Detail
from .FHIR_base64Binary import FHIR_base64Binary
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
FHIR_AuditEvent_Entity = TypedDict(
    "FHIR_AuditEvent_Entity",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifies a specific instance of the entity. The reference should be version specific.
        "what": FHIR_Reference,
        # The type of the object that was involved in this audit event.
        "type": FHIR_Coding,
        # Code representing the role the entity played in the event being audited.
        "role": FHIR_Coding,
        # Identifier for the data life-cycle stage for the entity.
        "lifecycle": FHIR_Coding,
        # Security labels for the identified entity.
        "securityLabel": List[FHIR_Coding],
        # A name of the entity in the audit event.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Text that describes the entity in more detail.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The query parameters for a query-type entities.
        "query": FHIR_base64Binary,
        # Extensions for query
        "_query": FHIR_Element,
        # Tagged value pairs for conveying additional information about the entity.
        "detail": List[FHIR_AuditEvent_Detail],
    },
    total=False,
)
