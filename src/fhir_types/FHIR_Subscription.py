from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_string import FHIR_string
from .FHIR_Subscription_Channel import FHIR_Subscription_Channel
from .FHIR_uri import FHIR_uri

# The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
FHIR_Subscription = TypedDict(
    "FHIR_Subscription",
    {
        # This is a Subscription resource
        "resourceType": Literal["Subscription"],
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
        # The status of the subscription, which marks the server state for managing the subscription.
        "status": Literal["requested", "active", "error", "off"],
        # Extensions for status
        "_status": FHIR_Element,
        # Contact details for a human to contact about the subscription. The primary use of this for system administrator troubleshooting.
        "contact": List[FHIR_ContactPoint],
        # The time for the server to turn the subscription off.
        "end": FHIR_instant,
        # Extensions for end
        "_end": FHIR_Element,
        # A description of why this subscription is defined.
        "reason": FHIR_string,
        # Extensions for reason
        "_reason": FHIR_Element,
        # The rules that the server should use to determine when to generate notifications for this subscription.
        "criteria": FHIR_string,
        # Extensions for criteria
        "_criteria": FHIR_Element,
        # A record of the last error that occurred when the server processed a notification.
        "error": FHIR_string,
        # Extensions for error
        "_error": FHIR_Element,
        # Details where to send notifications when resources are received that meet the criteria.
        "channel": FHIR_Subscription_Channel,
    },
    total=False,
)
