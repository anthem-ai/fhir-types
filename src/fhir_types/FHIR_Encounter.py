from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_Encounter_ClassHistory import FHIR_Encounter_ClassHistory
from .FHIR_Encounter_Diagnosis import FHIR_Encounter_Diagnosis
from .FHIR_Encounter_Hospitalization import FHIR_Encounter_Hospitalization
from .FHIR_Encounter_Location import FHIR_Encounter_Location
from .FHIR_Encounter_Participant import FHIR_Encounter_Participant
from .FHIR_Encounter_StatusHistory import FHIR_Encounter_StatusHistory
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
FHIR_Encounter = TypedDict(
    "FHIR_Encounter",
    {
        # This is a Encounter resource
        "resourceType": Literal["Encounter"],
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
        # Identifier(s) by which this encounter is known.
        "identifier": List[FHIR_Identifier],
        # planned | arrived | triaged | in-progress | onleave | finished | cancelled +.
        "status": Literal[
            "planned",
            "arrived",
            "triaged",
            "in-progress",
            "onleave",
            "finished",
            "cancelled",
            "entered-in-error",
            "unknown",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.
        "statusHistory": List[FHIR_Encounter_StatusHistory],
        # Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variations.
        "class": FHIR_Coding,
        # The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.
        "classHistory": List[FHIR_Encounter_ClassHistory],
        # Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation).
        "type": List[FHIR_CodeableConcept],
        # Broad categorization of the service that is to be provided (e.g. cardiology).
        "serviceType": FHIR_CodeableConcept,
        # Indicates the urgency of the encounter.
        "priority": FHIR_CodeableConcept,
        # The patient or group present at the encounter.
        "subject": FHIR_Reference,
        # Where a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem.  The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years).
        "episodeOfCare": List[FHIR_Reference],
        # The request this encounter satisfies (e.g. incoming referral or procedure request).
        "basedOn": List[FHIR_Reference],
        # The list of people responsible for providing the service.
        "participant": List[FHIR_Encounter_Participant],
        # The appointment that scheduled this encounter.
        "appointment": List[FHIR_Reference],
        # The start and end time of the encounter.
        "period": FHIR_Period,
        # Quantity of time the encounter lasted. This excludes the time during leaves of absence.
        "length": FHIR_Duration,
        # Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.
        "reasonCode": List[FHIR_CodeableConcept],
        # Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.
        "reasonReference": List[FHIR_Reference],
        # The list of diagnosis relevant to this encounter.
        "diagnosis": List[FHIR_Encounter_Diagnosis],
        # The set of accounts that may be used for billing for this Encounter.
        "account": List[FHIR_Reference],
        # Details about the admission to a healthcare service.
        "hospitalization": FHIR_Encounter_Hospitalization,
        # List of locations where  the patient has been during this encounter.
        "location": List[FHIR_Encounter_Location],
        # The organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation.  Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopy.
        "serviceProvider": FHIR_Reference,
        # Another Encounter of which this encounter is a part of (administratively or in time).
        "partOf": FHIR_Reference,
    },
    total=False,
)
