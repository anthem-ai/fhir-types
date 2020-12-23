from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_canonical import FHIR_canonical
from .FHIR_ChargeItem_Performer import FHIR_ChargeItem_Performer
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Money import FHIR_Money
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri

# The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
FHIR_ChargeItem = TypedDict(
    "FHIR_ChargeItem",
    {
        # This is a ChargeItem resource
        "resourceType": Literal["ChargeItem"],
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
        # Identifiers assigned to this event performer or other systems.
        "identifier": List[FHIR_Identifier],
        # References the (external) source of pricing information, rules of application for the code this ChargeItem uses.
        "definitionUri": List[FHIR_uri],
        # Extensions for definitionUri
        "_definitionUri": List[FHIR_Element],
        # References the source of pricing information, rules of application for the code this ChargeItem uses.
        "definitionCanonical": List[FHIR_canonical],
        # The current state of the ChargeItem.
        "status": Literal[
            "planned",
            "billable",
            "not-billable",
            "aborted",
            "billed",
            "entered-in-error",
            "unknown",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # ChargeItems can be grouped to larger ChargeItems covering the whole set.
        "partOf": List[FHIR_Reference],
        # A code that identifies the charge, like a billing code.
        "code": FHIR_CodeableConcept,
        # The individual or set of individuals the action is being or was performed on.
        "subject": FHIR_Reference,
        # The encounter or episode of care that establishes the context for this event.
        "context": FHIR_Reference,
        # Date/time(s) or duration when the charged service was applied.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # Date/time(s) or duration when the charged service was applied.
        "occurrencePeriod": FHIR_Period,
        # Date/time(s) or duration when the charged service was applied.
        "occurrenceTiming": FHIR_Timing,
        # Indicates who or what performed or participated in the charged service.
        "performer": List[FHIR_ChargeItem_Performer],
        # The organization requesting the service.
        "performingOrganization": FHIR_Reference,
        # The organization performing the service.
        "requestingOrganization": FHIR_Reference,
        # The financial cost center permits the tracking of charge attribution.
        "costCenter": FHIR_Reference,
        # Quantity of which the charge item has been serviced.
        "quantity": FHIR_Quantity,
        # The anatomical location where the related service has been applied.
        "bodysite": List[FHIR_CodeableConcept],
        # Factor overriding the factor determined by the rules associated with the code.
        "factorOverride": FHIR_decimal,
        # Extensions for factorOverride
        "_factorOverride": FHIR_Element,
        # Total price of the charge overriding the list price associated with the code.
        "priceOverride": FHIR_Money,
        # If the list price or the rule-based factor associated with the code is overridden, this attribute can capture a text to indicate the  reason for this action.
        "overrideReason": FHIR_string,
        # Extensions for overrideReason
        "_overrideReason": FHIR_Element,
        # The device, practitioner, etc. who entered the charge item.
        "enterer": FHIR_Reference,
        # Date the charge item was entered.
        "enteredDate": FHIR_dateTime,
        # Extensions for enteredDate
        "_enteredDate": FHIR_Element,
        # Describes why the event occurred in coded or textual form.
        "reason": List[FHIR_CodeableConcept],
        # Indicated the rendered service that caused this charge.
        "service": List[FHIR_Reference],
        # Identifies the device, food, drug or other product being charged either by type code or reference to an instance.
        "productReference": FHIR_Reference,
        # Identifies the device, food, drug or other product being charged either by type code or reference to an instance.
        "productCodeableConcept": FHIR_CodeableConcept,
        # Account into which this ChargeItems belongs.
        "account": List[FHIR_Reference],
        # Comments made about the event by the performer, subject or other participants.
        "note": List[FHIR_Annotation],
        # Further information supporting this charge.
        "supportingInformation": List[FHIR_Reference],
    },
    total=False,
)
