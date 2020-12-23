from typing import Any, List, Literal, TypedDict

from .FHIR_Age import FHIR_Age
from .FHIR_Annotation import FHIR_Annotation
from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_FamilyMemberHistory_Condition import FHIR_FamilyMemberHistory_Condition
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Significant health conditions for a person related to the patient relevant in the context of care for the patient.
FHIR_FamilyMemberHistory = TypedDict(
    "FHIR_FamilyMemberHistory",
    {
        # This is a FamilyMemberHistory resource
        "resourceType": Literal["FamilyMemberHistory"],
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
        # Business identifiers assigned to this family member history by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this FamilyMemberHistory.
        "instantiatesCanonical": List[FHIR_canonical],
        # The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this FamilyMemberHistory.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # A code specifying the status of the record of the family history of a specific family member.
        "status": Literal["partial", "completed", "entered-in-error", "health-unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # Describes why the family member's history is not available.
        "dataAbsentReason": FHIR_CodeableConcept,
        # The person who this history concerns.
        "patient": FHIR_Reference,
        # The date (and possibly time) when the family member history was recorded or last updated.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # This will either be a name or a description; e.g. "Aunt Susan", "my cousin with the red hair".
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # The type of relationship this person has to the patient (father, mother, brother etc.).
        "relationship": FHIR_CodeableConcept,
        # The birth sex of the family member.
        "sex": FHIR_CodeableConcept,
        # The actual or approximate date of birth of the relative.
        "bornPeriod": FHIR_Period,
        # The actual or approximate date of birth of the relative.
        "bornDate": str,
        # Extensions for bornDate
        "_bornDate": FHIR_Element,
        # The actual or approximate date of birth of the relative.
        "bornString": str,
        # Extensions for bornString
        "_bornString": FHIR_Element,
        # The age of the relative at the time the family member history is recorded.
        "ageAge": FHIR_Age,
        # The age of the relative at the time the family member history is recorded.
        "ageRange": FHIR_Range,
        # The age of the relative at the time the family member history is recorded.
        "ageString": str,
        # Extensions for ageString
        "_ageString": FHIR_Element,
        # If true, indicates that the age value specified is an estimated value.
        "estimatedAge": FHIR_boolean,
        # Extensions for estimatedAge
        "_estimatedAge": FHIR_Element,
        # Deceased flag or the actual or approximate age of the relative at the time of death for the family member history record.
        "deceasedBoolean": bool,
        # Extensions for deceasedBoolean
        "_deceasedBoolean": FHIR_Element,
        # Deceased flag or the actual or approximate age of the relative at the time of death for the family member history record.
        "deceasedAge": FHIR_Age,
        # Deceased flag or the actual or approximate age of the relative at the time of death for the family member history record.
        "deceasedRange": FHIR_Range,
        # Deceased flag or the actual or approximate age of the relative at the time of death for the family member history record.
        "deceasedDate": str,
        # Extensions for deceasedDate
        "_deceasedDate": FHIR_Element,
        # Deceased flag or the actual or approximate age of the relative at the time of death for the family member history record.
        "deceasedString": str,
        # Extensions for deceasedString
        "_deceasedString": FHIR_Element,
        # Describes why the family member history occurred in coded or textual form.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates a Condition, Observation, AllergyIntolerance, or QuestionnaireResponse that justifies this family member history event.
        "reasonReference": List[FHIR_Reference],
        # This property allows a non condition-specific note to the made about the related person. Ideally, the note would be in the condition property, but this is not always possible.
        "note": List[FHIR_Annotation],
        # The significant Conditions (or condition) that the family member had. This is a repeating section to allow a system to represent more than one condition per resource, though there is nothing stopping multiple resources - one per condition.
        "condition": List[FHIR_FamilyMemberHistory_Condition],
    },
    total=False,
)
