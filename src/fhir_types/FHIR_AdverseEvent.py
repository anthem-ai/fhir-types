from typing import Any, List, Literal, TypedDict

from .FHIR_AdverseEvent_SuspectEntity import FHIR_AdverseEvent_SuspectEntity
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
FHIR_AdverseEvent = TypedDict(
    "FHIR_AdverseEvent",
    {
        # This is a AdverseEvent resource
        "resourceType": Literal["AdverseEvent"],
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
        # Business identifiers assigned to this adverse event by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": FHIR_Identifier,
        # Whether the event actually happened, or just had the potential to. Note that this is independent of whether anyone was affected or harmed or how severely.
        "actuality": Literal["actual", "potential"],
        # Extensions for actuality
        "_actuality": FHIR_Element,
        # The overall type of event, intended for search and filtering purposes.
        "category": List[FHIR_CodeableConcept],
        # This element defines the specific type of event that occurred or that was prevented from occurring.
        "event": FHIR_CodeableConcept,
        # This subject or group impacted by the event.
        "subject": FHIR_Reference,
        # The Encounter during which AdverseEvent was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # The date (and perhaps time) when the adverse event occurred.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Estimated or actual date the AdverseEvent began, in the opinion of the reporter.
        "detected": FHIR_dateTime,
        # Extensions for detected
        "_detected": FHIR_Element,
        # The date on which the existence of the AdverseEvent was first recorded.
        "recordedDate": FHIR_dateTime,
        # Extensions for recordedDate
        "_recordedDate": FHIR_Element,
        # Includes information about the reaction that occurred as a result of exposure to a substance (for example, a drug or a chemical).
        "resultingCondition": List[FHIR_Reference],
        # The information about where the adverse event occurred.
        "location": FHIR_Reference,
        # Assessment whether this event was of real importance.
        "seriousness": FHIR_CodeableConcept,
        # Describes the severity of the adverse event, in relation to the subject. Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but a mild heart problem is.
        "severity": FHIR_CodeableConcept,
        # Describes the type of outcome from the adverse event.
        "outcome": FHIR_CodeableConcept,
        # Information on who recorded the adverse event.  May be the patient or a practitioner.
        "recorder": FHIR_Reference,
        # Parties that may or should contribute or have contributed information to the adverse event, which can consist of one or more activities.  Such information includes information leading to the decision to perform the activity and how to perform the activity (e.g. consultant), information that the activity itself seeks to reveal (e.g. informant of clinical history), or information about what activity was performed (e.g. informant witness).
        "contributor": List[FHIR_Reference],
        # Describes the entity that is suspected to have caused the adverse event.
        "suspectEntity": List[FHIR_AdverseEvent_SuspectEntity],
        # AdverseEvent.subjectMedicalHistory.
        "subjectMedicalHistory": List[FHIR_Reference],
        # AdverseEvent.referenceDocument.
        "referenceDocument": List[FHIR_Reference],
        # AdverseEvent.study.
        "study": List[FHIR_Reference],
    },
    total=False,
)
