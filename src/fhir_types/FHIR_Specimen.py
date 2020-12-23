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
from .FHIR_Reference import FHIR_Reference
from .FHIR_Specimen_Collection import FHIR_Specimen_Collection
from .FHIR_Specimen_Container import FHIR_Specimen_Container
from .FHIR_Specimen_Processing import FHIR_Specimen_Processing
from .FHIR_uri import FHIR_uri

# A sample to be used for analysis.
FHIR_Specimen = TypedDict(
    "FHIR_Specimen",
    {
        # This is a Specimen resource
        "resourceType": Literal["Specimen"],
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
        # Id for specimen.
        "identifier": List[FHIR_Identifier],
        # The identifier assigned by the lab when accessioning specimen(s). This is not necessarily the same as the specimen identifier, depending on local lab procedures.
        "accessionIdentifier": FHIR_Identifier,
        # The availability of the specimen.
        "status": Literal[
            "available", "unavailable", "unsatisfactory", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # The kind of material that forms the specimen.
        "type": FHIR_CodeableConcept,
        # Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device.
        "subject": FHIR_Reference,
        # Time when specimen was received for processing or testing.
        "receivedTime": FHIR_dateTime,
        # Extensions for receivedTime
        "_receivedTime": FHIR_Element,
        # Reference to the parent (source) specimen which is used when the specimen was either derived from or a component of another specimen.
        "parent": List[FHIR_Reference],
        # Details concerning a service request that required a specimen to be collected.
        "request": List[FHIR_Reference],
        # Details concerning the specimen collection.
        "collection": FHIR_Specimen_Collection,
        # Details concerning processing and processing steps for the specimen.
        "processing": List[FHIR_Specimen_Processing],
        # The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.
        "container": List[FHIR_Specimen_Container],
        # A mode or state of being that describes the nature of the specimen.
        "condition": List[FHIR_CodeableConcept],
        # To communicate any details or issues about the specimen or during the specimen collection. (for example: broken vial, sent with patient, frozen).
        "note": List[FHIR_Annotation],
    },
    total=False,
)
