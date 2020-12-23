from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Composition_Attester import FHIR_Composition_Attester
from .FHIR_Composition_Event import FHIR_Composition_Event
from .FHIR_Composition_RelatesTo import FHIR_Composition_RelatesTo
from .FHIR_Composition_Section import FHIR_Composition_Section
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
FHIR_Composition = TypedDict(
    "FHIR_Composition",
    {
        # This is a Composition resource
        "resourceType": Literal["Composition"],
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
        # A version-independent identifier for the Composition. This identifier stays constant as the composition is changed over time.
        "identifier": FHIR_Identifier,
        # The workflow/clinical status of this composition. The status is a marker for the clinical standing of the document.
        "status": Literal["preliminary", "final", "amended", "entered-in-error"],
        # Extensions for status
        "_status": FHIR_Element,
        # Specifies the particular kind of composition (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the composition.
        "type": FHIR_CodeableConcept,
        # A categorization for the type of the composition - helps for indexing and searching. This may be implied by or derived from the code specified in the Composition Type.
        "category": List[FHIR_CodeableConcept],
        # Who or what the composition is about. The composition can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of livestock, or a set of patients that share a common exposure).
        "subject": FHIR_Reference,
        # Describes the clinical encounter or type of care this documentation is associated with.
        "encounter": FHIR_Reference,
        # The composition editing time, when the composition was last logically changed by the author.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Identifies who is responsible for the information in the composition, not necessarily who typed it in.
        "author": List[FHIR_Reference],
        # Official human-readable label for the composition.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # The code specifying the level of confidentiality of the Composition.
        "confidentiality": FHIR_code,
        # Extensions for confidentiality
        "_confidentiality": FHIR_Element,
        # A participant who has attested to the accuracy of the composition/document.
        "attester": List[FHIR_Composition_Attester],
        # Identifies the organization or group who is responsible for ongoing maintenance of and access to the composition/document information.
        "custodian": FHIR_Reference,
        # Relationships that this composition has with other compositions or documents that already exist.
        "relatesTo": List[FHIR_Composition_RelatesTo],
        # The clinical service, such as a colonoscopy or an appendectomy, being documented.
        "event": List[FHIR_Composition_Event],
        # The root of the sections that make up the composition.
        "section": List[FHIR_Composition_Section],
    },
    total=False,
)
