from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_CareTeam_Participant import FHIR_CareTeam_Participant
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
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

# The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
FHIR_CareTeam = TypedDict(
    "FHIR_CareTeam",
    {
        # This is a CareTeam resource
        "resourceType": Literal["CareTeam"],
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
        # Business identifiers assigned to this care team by the performer or other systems which remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # Indicates the current state of the care team.
        "status": Literal[
            "proposed", "active", "suspended", "inactive", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # Identifies what kind of team.  This is to support differentiation between multiple co-existing teams, such as care plan team, episode of care team, longitudinal care team.
        "category": List[FHIR_CodeableConcept],
        # A label for human use intended to distinguish like teams.  E.g. the "red" vs. "green" trauma teams.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Identifies the patient or group whose intended care is handled by the team.
        "subject": FHIR_Reference,
        # The Encounter during which this CareTeam was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # Indicates when the team did (or is intended to) come into effect and end.
        "period": FHIR_Period,
        # Identifies all people and organizations who are expected to be involved in the care team.
        "participant": List[FHIR_CareTeam_Participant],
        # Describes why the care team exists.
        "reasonCode": List[FHIR_CodeableConcept],
        # Condition(s) that this care team addresses.
        "reasonReference": List[FHIR_Reference],
        # The organization responsible for the care team.
        "managingOrganization": List[FHIR_Reference],
        # A central contact detail for the care team (that applies to all members).
        "telecom": List[FHIR_ContactPoint],
        # Comments made about the CareTeam.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
