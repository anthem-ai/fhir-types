from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Moiety = TypedDict(
    "FHIR_SubstanceSpecification_Moiety",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Role that the moiety is playing.
        "role": FHIR_CodeableConcept,
        # Identifier by which this moiety substance is known.
        "identifier": FHIR_Identifier,
        # Textual name for this moiety substance.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Stereochemistry type.
        "stereochemistry": FHIR_CodeableConcept,
        # Optical activity type.
        "opticalActivity": FHIR_CodeableConcept,
        # Molecular formula.
        "molecularFormula": FHIR_string,
        # Extensions for molecularFormula
        "_molecularFormula": FHIR_Element,
        # Quantitative value for this moiety.
        "amountQuantity": FHIR_Quantity,
        # Quantitative value for this moiety.
        "amountString": str,
        # Extensions for amountString
        "_amountString": FHIR_Element,
    },
    total=False,
)
