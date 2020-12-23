from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri

# A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
FHIR_DeviceUseStatement = TypedDict(
    "FHIR_DeviceUseStatement",
    {
        # This is a DeviceUseStatement resource
        "resourceType": Literal["DeviceUseStatement"],
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
        # An external identifier for this statement such as an IRI.
        "identifier": List[FHIR_Identifier],
        # A plan, proposal or order that is fulfilled in whole or in part by this DeviceUseStatement.
        "basedOn": List[FHIR_Reference],
        # A code representing the patient or other source's judgment about the state of the device used that this statement is about.  Generally this will be active or completed.
        "status": Literal[
            "active", "completed", "entered-in-error", "intended", "stopped", "on-hold"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The patient who used the device.
        "subject": FHIR_Reference,
        # Allows linking the DeviceUseStatement to the underlying Request, or to other information that supports or is used to derive the DeviceUseStatement.
        "derivedFrom": List[FHIR_Reference],
        # How often the device was used.
        "timingTiming": FHIR_Timing,
        # How often the device was used.
        "timingPeriod": FHIR_Period,
        # How often the device was used.
        "timingDateTime": str,
        # Extensions for timingDateTime
        "_timingDateTime": FHIR_Element,
        # The time at which the statement was made/recorded.
        "recordedOn": FHIR_dateTime,
        # Extensions for recordedOn
        "_recordedOn": FHIR_Element,
        # Who reported the device was being used by the patient.
        "source": FHIR_Reference,
        # The details of the device used.
        "device": FHIR_Reference,
        # Reason or justification for the use of the device.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource whose existence justifies this DeviceUseStatement.
        "reasonReference": List[FHIR_Reference],
        # Indicates the anotomic location on the subject's body where the device was used ( i.e. the target).
        "bodySite": FHIR_CodeableConcept,
        # Details about the device statement that were not represented at all or sufficiently in one of the attributes provided in a class. These may include for example a comment, an instruction, or a note associated with the statement.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
