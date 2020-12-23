from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_SubstanceSpecification_Code import FHIR_SubstanceSpecification_Code
from .FHIR_SubstanceSpecification_Moiety import FHIR_SubstanceSpecification_Moiety
from .FHIR_SubstanceSpecification_MolecularWeight import (
    FHIR_SubstanceSpecification_MolecularWeight,
)
from .FHIR_SubstanceSpecification_Name import FHIR_SubstanceSpecification_Name
from .FHIR_SubstanceSpecification_Property import FHIR_SubstanceSpecification_Property
from .FHIR_SubstanceSpecification_Relationship import (
    FHIR_SubstanceSpecification_Relationship,
)
from .FHIR_SubstanceSpecification_Structure import FHIR_SubstanceSpecification_Structure
from .FHIR_uri import FHIR_uri

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification = TypedDict(
    "FHIR_SubstanceSpecification",
    {
        # This is a SubstanceSpecification resource
        "resourceType": Literal["SubstanceSpecification"],
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
        # Identifier by which this substance is known.
        "identifier": FHIR_Identifier,
        # High level categorization, e.g. polymer or nucleic acid.
        "type": FHIR_CodeableConcept,
        # Status of substance within the catalogue e.g. approved.
        "status": FHIR_CodeableConcept,
        # If the substance applies to only human or veterinary use.
        "domain": FHIR_CodeableConcept,
        # Textual description of the substance.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Supporting literature.
        "source": List[FHIR_Reference],
        # Textual comment about this record of a substance.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
        # Moiety, for structural modifications.
        "moiety": List[FHIR_SubstanceSpecification_Moiety],
        # General specifications for this substance, including how it is related to other substances.
        "property": List[FHIR_SubstanceSpecification_Property],
        # General information detailing this substance.
        "referenceInformation": FHIR_Reference,
        # Structural information.
        "structure": FHIR_SubstanceSpecification_Structure,
        # Codes associated with the substance.
        "code": List[FHIR_SubstanceSpecification_Code],
        # Names applicable to this substance.
        "name": List[FHIR_SubstanceSpecification_Name],
        # The molecular weight or weight range (for proteins, polymers or nucleic acids).
        "molecularWeight": List[FHIR_SubstanceSpecification_MolecularWeight],
        # A link between this substance and another, with details of the relationship.
        "relationship": List[FHIR_SubstanceSpecification_Relationship],
        # Data items specific to nucleic acids.
        "nucleicAcid": FHIR_Reference,
        # Data items specific to polymers.
        "polymer": FHIR_Reference,
        # Data items specific to proteins.
        "protein": FHIR_Reference,
        # Material or taxonomic/anatomical source for the substance.
        "sourceMaterial": FHIR_Reference,
    },
    total=False,
)
