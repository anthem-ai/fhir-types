from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_MedicationAdministration_Dosage import FHIR_MedicationAdministration_Dosage
from .FHIR_MedicationAdministration_Performer import (
    FHIR_MedicationAdministration_Performer,
)
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
FHIR_MedicationAdministration = TypedDict(
    "FHIR_MedicationAdministration",
    {
        # This is a MedicationAdministration resource
        "resourceType": Literal["MedicationAdministration"],
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
        # Identifiers associated with this Medication Administration that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # A protocol, guideline, orderset, or other definition that was adhered to in whole or in part by this event.
        "instantiates": List[FHIR_uri],
        # Extensions for instantiates
        "_instantiates": List[FHIR_Element],
        # A larger event of which this particular event is a component or step.
        "partOf": List[FHIR_Reference],
        # Will generally be set to show that the administration has been completed.  For some long running administrations such as infusions, it is possible for an administration to be started but not completed or it may be paused while some other process is under way.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # A code indicating why the administration was not performed.
        "statusReason": List[FHIR_CodeableConcept],
        # Indicates where the medication is expected to be consumed or administered.
        "category": FHIR_CodeableConcept,
        # Identifies the medication that was administered. This is either a link to a resource representing the details of the medication or a simple attribute carrying a code that identifies the medication from a known list of medications.
        "medicationCodeableConcept": FHIR_CodeableConcept,
        # Identifies the medication that was administered. This is either a link to a resource representing the details of the medication or a simple attribute carrying a code that identifies the medication from a known list of medications.
        "medicationReference": FHIR_Reference,
        # The person or animal or group receiving the medication.
        "subject": FHIR_Reference,
        # The visit, admission, or other contact between patient and health care provider during which the medication administration was performed.
        "context": FHIR_Reference,
        # Additional information (for example, patient height and weight) that supports the administration of the medication.
        "supportingInformation": List[FHIR_Reference],
        # A specific date/time or interval of time during which the administration took place (or did not take place, when the 'notGiven' attribute is true). For many administrations, such as swallowing a tablet the use of dateTime is more appropriate.
        "effectiveDateTime": str,
        # Extensions for effectiveDateTime
        "_effectiveDateTime": FHIR_Element,
        # A specific date/time or interval of time during which the administration took place (or did not take place, when the 'notGiven' attribute is true). For many administrations, such as swallowing a tablet the use of dateTime is more appropriate.
        "effectivePeriod": FHIR_Period,
        # Indicates who or what performed the medication administration and how they were involved.
        "performer": List[FHIR_MedicationAdministration_Performer],
        # A code indicating why the medication was given.
        "reasonCode": List[FHIR_CodeableConcept],
        # Condition or observation that supports why the medication was administered.
        "reasonReference": List[FHIR_Reference],
        # The original request, instruction or authority to perform the administration.
        "request": FHIR_Reference,
        # The device used in administering the medication to the patient.  For example, a particular infusion pump.
        "device": List[FHIR_Reference],
        # Extra information about the medication administration that is not conveyed by the other attributes.
        "note": List[FHIR_Annotation],
        # Describes the medication dosage information details e.g. dose, rate, site, route, etc.
        "dosage": FHIR_MedicationAdministration_Dosage,
        # A summary of the events of interest that have occurred, such as when the administration was verified.
        "eventHistory": List[FHIR_Reference],
    },
    total=False,
)
