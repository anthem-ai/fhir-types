from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_SupplyDelivery_SuppliedItem import FHIR_SupplyDelivery_SuppliedItem
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri

# Record of delivery of what is supplied.
FHIR_SupplyDelivery = TypedDict(
    "FHIR_SupplyDelivery",
    {
        # This is a SupplyDelivery resource
        "resourceType": Literal["SupplyDelivery"],
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
        # Identifier for the supply delivery event that is used to identify it across multiple disparate systems.
        "identifier": List[FHIR_Identifier],
        # A plan, proposal or order that is fulfilled in whole or in part by this event.
        "basedOn": List[FHIR_Reference],
        # A larger event of which this particular event is a component or step.
        "partOf": List[FHIR_Reference],
        # A code specifying the state of the dispense event.
        "status": Literal["in-progress", "completed", "abandoned", "entered-in-error"],
        # Extensions for status
        "_status": FHIR_Element,
        # A link to a resource representing the person whom the delivered item is for.
        "patient": FHIR_Reference,
        # Indicates the type of dispensing event that is performed. Examples include: Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
        "type": FHIR_CodeableConcept,
        # The item that is being delivered or has been supplied.
        "suppliedItem": FHIR_SupplyDelivery_SuppliedItem,
        # The date or time(s) the activity occurred.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # The date or time(s) the activity occurred.
        "occurrencePeriod": FHIR_Period,
        # The date or time(s) the activity occurred.
        "occurrenceTiming": FHIR_Timing,
        # The individual responsible for dispensing the medication, supplier or device.
        "supplier": FHIR_Reference,
        # Identification of the facility/location where the Supply was shipped to, as part of the dispense event.
        "destination": FHIR_Reference,
        # Identifies the person who picked up the Supply.
        "receiver": List[FHIR_Reference],
    },
    total=False,
)
