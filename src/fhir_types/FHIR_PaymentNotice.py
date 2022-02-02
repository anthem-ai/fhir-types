from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Money import FHIR_Money
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
FHIR_PaymentNotice = TypedDict(
    "FHIR_PaymentNotice",
    {
        # This is a PaymentNotice resource
        "resourceType": Literal["PaymentNotice"],
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
        # A unique identifier assigned to this payment notice.
        "identifier": List[FHIR_Identifier],
        # The status of the resource instance.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Reference of resource for which payment is being made.
        "request": FHIR_Reference,
        # Reference of response to resource for which payment is being made.
        "response": FHIR_Reference,
        # The date when this resource was created.
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # The practitioner who is responsible for the services rendered to the patient.
        "provider": FHIR_Reference,
        # A reference to the payment which is the subject of this notice.
        "payment": FHIR_Reference,
        # The date when the above payment action occurred.
        "paymentDate": FHIR_date,
        # Extensions for paymentDate
        "_paymentDate": FHIR_Element,
        # The party who will receive or has received payment that is the subject of this notification.
        "payee": FHIR_Reference,
        # The party who is notified of the payment status.
        "recipient": FHIR_Reference,
        # The amount sent to the payee.
        "amount": FHIR_Money,
        # A code indicating whether payment has been sent or cleared.
        "paymentStatus": FHIR_CodeableConcept,
    },
    total=False,
)
