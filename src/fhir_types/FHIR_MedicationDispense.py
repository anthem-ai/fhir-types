from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Dosage import FHIR_Dosage
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_MedicationDispense_Performer import FHIR_MedicationDispense_Performer
from .FHIR_MedicationDispense_Substitution import FHIR_MedicationDispense_Substitution
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
FHIR_MedicationDispense = TypedDict(
    "FHIR_MedicationDispense",
    {
        # This is a MedicationDispense resource
        "resourceType": Literal["MedicationDispense"],
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
        # Identifiers associated with this Medication Dispense that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # The procedure that trigger the dispense.
        "partOf": List[FHIR_Reference],
        # A code specifying the state of the set of dispense events.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Indicates the reason why a dispense was not performed.
        "statusReasonCodeableConcept": FHIR_CodeableConcept,
        # Indicates the reason why a dispense was not performed.
        "statusReasonReference": FHIR_Reference,
        # Indicates the type of medication dispense (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient)).
        "category": FHIR_CodeableConcept,
        # Identifies the medication being administered. This is either a link to a resource representing the details of the medication or a simple attribute carrying a code that identifies the medication from a known list of medications.
        "medicationCodeableConcept": FHIR_CodeableConcept,
        # Identifies the medication being administered. This is either a link to a resource representing the details of the medication or a simple attribute carrying a code that identifies the medication from a known list of medications.
        "medicationReference": FHIR_Reference,
        # A link to a resource representing the person or the group to whom the medication will be given.
        "subject": FHIR_Reference,
        # The encounter or episode of care that establishes the context for this event.
        "context": FHIR_Reference,
        # Additional information that supports the medication being dispensed.
        "supportingInformation": List[FHIR_Reference],
        # Indicates who or what performed the event.
        "performer": List[FHIR_MedicationDispense_Performer],
        # The principal physical location where the dispense was performed.
        "location": FHIR_Reference,
        # Indicates the medication order that is being dispensed against.
        "authorizingPrescription": List[FHIR_Reference],
        # Indicates the type of dispensing event that is performed. For example, Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
        "type": FHIR_CodeableConcept,
        # The amount of medication that has been dispensed. Includes unit of measure.
        "quantity": FHIR_Quantity,
        # The amount of medication expressed as a timing amount.
        "daysSupply": FHIR_Quantity,
        # The time when the dispensed product was packaged and reviewed.
        "whenPrepared": FHIR_dateTime,
        # Extensions for whenPrepared
        "_whenPrepared": FHIR_Element,
        # The time the dispensed product was provided to the patient or their representative.
        "whenHandedOver": FHIR_dateTime,
        # Extensions for whenHandedOver
        "_whenHandedOver": FHIR_Element,
        # Identification of the facility/location where the medication was shipped to, as part of the dispense event.
        "destination": FHIR_Reference,
        # Identifies the person who picked up the medication.  This will usually be a patient or their caregiver, but some cases exist where it can be a healthcare professional.
        "receiver": List[FHIR_Reference],
        # Extra information about the dispense that could not be conveyed in the other attributes.
        "note": List[FHIR_Annotation],
        # Indicates how the medication is to be used by the patient.
        "dosageInstruction": List[FHIR_Dosage],
        # Indicates whether or not substitution was made as part of the dispense.  In some cases, substitution will be expected but does not happen, in other cases substitution is not expected but does happen.  This block explains what substitution did or did not happen and why.  If nothing is specified, substitution was not done.
        "substitution": FHIR_MedicationDispense_Substitution,
        # Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. drug-drug interaction, duplicate therapy, dosage alert etc.
        "detectedIssue": List[FHIR_Reference],
        # A summary of the events of interest that have occurred, such as when the dispense was verified.
        "eventHistory": List[FHIR_Reference],
    },
    total=False,
)
