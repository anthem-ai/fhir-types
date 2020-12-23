from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
FHIR_BodyStructure = TypedDict(
    "FHIR_BodyStructure",
    {
        # This is a BodyStructure resource
        "resourceType": Literal["BodyStructure"],
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
        # Identifier for this instance of the anatomical structure.
        "identifier": List[FHIR_Identifier],
        # Whether this body site is in active use.
        "active": FHIR_boolean,
        # Extensions for active
        "_active": FHIR_Element,
        # The kind of structure being represented by the body structure at `BodyStructure.location`.  This can define both normal and abnormal morphologies.
        "morphology": FHIR_CodeableConcept,
        # The anatomical location or region of the specimen, lesion, or body structure.
        "location": FHIR_CodeableConcept,
        # Qualifier to refine the anatomical location.  These include qualifiers for laterality, relative location, directionality, number, and plane.
        "locationQualifier": List[FHIR_CodeableConcept],
        # A summary, characterization or explanation of the body structure.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Image or images used to identify a location.
        "image": List[FHIR_Attachment],
        # The person to which the body site belongs.
        "patient": FHIR_Reference,
    },
    total=False,
)
