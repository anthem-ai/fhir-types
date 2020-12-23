from typing import Any, List, Literal, TypedDict

from .FHIR_AuditEvent_Network import FHIR_AuditEvent_Network
from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
FHIR_AuditEvent_Agent = TypedDict(
    "FHIR_AuditEvent_Agent",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Specification of the participation type the user plays when performing the event.
        "type": FHIR_CodeableConcept,
        # The security role that the user was acting under, that come from local codes defined by the access control security system (e.g. RBAC, ABAC) used in the local context.
        "role": List[FHIR_CodeableConcept],
        # Reference to who this agent is that was involved in the event.
        "who": FHIR_Reference,
        # Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system (e.g. single sign-on), if available.
        "altId": FHIR_string,
        # Extensions for altId
        "_altId": FHIR_Element,
        # Human-meaningful name for the agent.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Indicator that the user is or is not the requestor, or initiator, for the event being audited.
        "requestor": FHIR_boolean,
        # Extensions for requestor
        "_requestor": FHIR_Element,
        # Where the event occurred.
        "location": FHIR_Reference,
        # The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.
        "policy": List[FHIR_uri],
        # Extensions for policy
        "_policy": List[FHIR_Element],
        # Type of media involved. Used when the event is about exporting/importing onto media.
        "media": FHIR_Coding,
        # Logical network location for application activity, if the activity has a network location.
        "network": FHIR_AuditEvent_Network,
        # The reason (purpose of use), specific to this agent, that was used during the event being recorded.
        "purposeOfUse": List[FHIR_CodeableConcept],
    },
    total=False,
)
