from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_DocumentManifest_Related import FHIR_DocumentManifest_Related
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A collection of documents compiled for a purpose together with metadata that applies to the collection.
FHIR_DocumentManifest = TypedDict(
    "FHIR_DocumentManifest",
    {
        # This is a DocumentManifest resource
        "resourceType": Literal["DocumentManifest"],
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
        # A single identifier that uniquely identifies this manifest. Principally used to refer to the manifest in non-FHIR contexts.
        "masterIdentifier": FHIR_Identifier,
        # Other identifiers associated with the document manifest, including version independent  identifiers.
        "identifier": List[FHIR_Identifier],
        # The status of this document manifest.
        "status": Literal["current", "superseded", "entered-in-error"],
        # Extensions for status
        "_status": FHIR_Element,
        # The code specifying the type of clinical activity that resulted in placing the associated content into the DocumentManifest.
        "type": FHIR_CodeableConcept,
        # Who or what the set of documents is about. The documents can be about a person, (patient or healthcare practitioner), a device (i.e. machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure). If the documents cross more than one subject, then more than one subject is allowed here (unusual use case).
        "subject": FHIR_Reference,
        # When the document manifest was created for submission to the server (not necessarily the same thing as the actual resource last modified time, since it may be modified, replicated, etc.).
        "created": FHIR_dateTime,
        # Extensions for created
        "_created": FHIR_Element,
        # Identifies who is the author of the manifest. Manifest author is not necessarly the author of the references included.
        "author": List[FHIR_Reference],
        # A patient, practitioner, or organization for which this set of documents is intended.
        "recipient": List[FHIR_Reference],
        # Identifies the source system, application, or software that produced the document manifest.
        "source": FHIR_uri,
        # Extensions for source
        "_source": FHIR_Element,
        # Human-readable description of the source document. This is sometimes known as the "title".
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The list of Resources that consist of the parts of this manifest.
        "content": List[FHIR_Reference],
        # Related identifiers or resources associated with the DocumentManifest.
        "related": List[FHIR_DocumentManifest_Related],
    },
    total=False,
)
