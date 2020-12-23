from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_SubstanceSpecification_Isotope import FHIR_SubstanceSpecification_Isotope
from .FHIR_SubstanceSpecification_MolecularWeight import (
    FHIR_SubstanceSpecification_MolecularWeight,
)
from .FHIR_SubstanceSpecification_Representation import (
    FHIR_SubstanceSpecification_Representation,
)

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Structure = TypedDict(
    "FHIR_SubstanceSpecification_Structure",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Stereochemistry type.
        "stereochemistry": FHIR_CodeableConcept,
        # Optical activity type.
        "opticalActivity": FHIR_CodeableConcept,
        # Molecular formula.
        "molecularFormula": FHIR_string,
        # Extensions for molecularFormula
        "_molecularFormula": FHIR_Element,
        # Specified per moiety according to the Hill system, i.e. first C, then H, then alphabetical, each moiety separated by a dot.
        "molecularFormulaByMoiety": FHIR_string,
        # Extensions for molecularFormulaByMoiety
        "_molecularFormulaByMoiety": FHIR_Element,
        # Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio.
        "isotope": List[FHIR_SubstanceSpecification_Isotope],
        # The molecular weight or weight range (for proteins, polymers or nucleic acids).
        "molecularWeight": FHIR_SubstanceSpecification_MolecularWeight,
        # Supporting literature.
        "source": List[FHIR_Reference],
        # Molecular structural representation.
        "representation": List[FHIR_SubstanceSpecification_Representation],
    },
    total=False,
)
