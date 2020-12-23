from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_url import FHIR_url

# The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
FHIR_Endpoint = TypedDict(
    "FHIR_Endpoint",
    {
        # This is a Endpoint resource
        "resourceType": Literal["Endpoint"],
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
        # Identifier for the organization that is used to identify the endpoint across multiple disparate systems.
        "identifier": List[FHIR_Identifier],
        # active | suspended | error | off | test.
        "status": Literal[
            "active", "suspended", "error", "off", "entered-in-error", "test"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # A coded value that represents the technical details of the usage of this endpoint, such as what WSDLs should be used in what way. (e.g. XDS.b/DICOM/cds-hook).
        "connectionType": FHIR_Coding,
        # A friendly name that this endpoint can be referred to with.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # The organization that manages this endpoint (even if technically another organization is hosting this in the cloud, it is the organization associated with the data).
        "managingOrganization": FHIR_Reference,
        # Contact details for a human to contact about the subscription. The primary use of this for system administrator troubleshooting.
        "contact": List[FHIR_ContactPoint],
        # The interval during which the endpoint is expected to be operational.
        "period": FHIR_Period,
        # The payload type describes the acceptable content that can be communicated on the endpoint.
        "payloadType": List[FHIR_CodeableConcept],
        # The mime type to send the payload in - e.g. application/fhir+xml, application/fhir+json. If the mime type is not specified, then the sender could send any content (including no content depending on the connectionType).
        "payloadMimeType": List[FHIR_code],
        # Extensions for payloadMimeType
        "_payloadMimeType": List[FHIR_Element],
        # The uri that describes the actual end-point to connect to.
        "address": FHIR_url,
        # Extensions for address
        "_address": FHIR_Element,
        # Additional headers / information to send as part of the notification.
        "header": List[FHIR_string],
        # Extensions for header
        "_header": List[FHIR_Element],
    },
    total=False,
)
