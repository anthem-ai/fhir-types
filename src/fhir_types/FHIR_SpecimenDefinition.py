from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_SpecimenDefinition_TypeTested import FHIR_SpecimenDefinition_TypeTested
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A kind of specimen with associated set of requirements.
FHIR_SpecimenDefinition = TypedDict(
    "FHIR_SpecimenDefinition",
    {
        # This is a SpecimenDefinition resource
        "resourceType": Literal["SpecimenDefinition"],
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
        # A business identifier associated with the kind of specimen.
        "identifier": FHIR_Identifier,
        # The kind of material to be collected.
        "typeCollected": FHIR_CodeableConcept,
        # Preparation of the patient for specimen collection.
        "patientPreparation": List[FHIR_CodeableConcept],
        # Time aspect of specimen collection (duration or offset).
        "timeAspect": FHIR_string,
        # Extensions for timeAspect
        "_timeAspect": FHIR_Element,
        # The action to be performed for collecting the specimen.
        "collection": List[FHIR_CodeableConcept],
        # Specimen conditioned in a container as expected by the testing laboratory.
        "typeTested": List[FHIR_SpecimenDefinition_TypeTested],
    },
    total=False,
)
