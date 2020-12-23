from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Provenance_Agent import FHIR_Provenance_Agent
from .FHIR_Provenance_Entity import FHIR_Provenance_Entity
from .FHIR_Reference import FHIR_Reference
from .FHIR_Signature import FHIR_Signature
from .FHIR_uri import FHIR_uri

# Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.
FHIR_Provenance = TypedDict(
    "FHIR_Provenance",
    {
        # This is a Provenance resource
        "resourceType": Literal["Provenance"],
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
        # The Reference(s) that were generated or updated by  the activity described in this resource. A provenance can point to more than one target if multiple resources were created/updated by the same activity.
        "target": List[FHIR_Reference],
        # The period during which the activity occurred.
        "occurredPeriod": FHIR_Period,
        # The period during which the activity occurred.
        "occurredDateTime": str,
        # Extensions for occurredDateTime
        "_occurredDateTime": FHIR_Element,
        # The instant of time at which the activity was recorded.
        "recorded": FHIR_instant,
        # Extensions for recorded
        "_recorded": FHIR_Element,
        # Policy or plan the activity was defined by. Typically, a single activity may have multiple applicable policy documents, such as patient consent, guarantor funding, etc.
        "policy": List[FHIR_uri],
        # Extensions for policy
        "_policy": List[FHIR_Element],
        # Where the activity occurred, if relevant.
        "location": FHIR_Reference,
        # The reason that the activity was taking place.
        "reason": List[FHIR_CodeableConcept],
        # An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
        "activity": FHIR_CodeableConcept,
        # An actor taking a role in an activity  for which it can be assigned some degree of responsibility for the activity taking place.
        "agent": List[FHIR_Provenance_Agent],
        # An entity used in this activity.
        "entity": List[FHIR_Provenance_Entity],
        # A digital signature on the target Reference(s). The signer should match a Provenance.agent. The purpose of the signature is indicated.
        "signature": List[FHIR_Signature],
    },
    total=False,
)
