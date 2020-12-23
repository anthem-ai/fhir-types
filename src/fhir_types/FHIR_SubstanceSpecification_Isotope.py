from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string
from .FHIR_SubstanceSpecification_MolecularWeight import (
    FHIR_SubstanceSpecification_MolecularWeight,
)

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Isotope = TypedDict(
    "FHIR_SubstanceSpecification_Isotope",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Substance identifier for each non-natural or radioisotope.
        "identifier": FHIR_Identifier,
        # Substance name for each non-natural or radioisotope.
        "name": FHIR_CodeableConcept,
        # The type of isotopic substitution present in a single substance.
        "substitution": FHIR_CodeableConcept,
        # Half life - for a non-natural nuclide.
        "halfLife": FHIR_Quantity,
        # The molecular weight or weight range (for proteins, polymers or nucleic acids).
        "molecularWeight": FHIR_SubstanceSpecification_MolecularWeight,
    },
    total=False,
)
