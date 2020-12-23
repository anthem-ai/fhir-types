from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_MolecularSequence_Inner import FHIR_MolecularSequence_Inner
from .FHIR_MolecularSequence_Outer import FHIR_MolecularSequence_Outer
from .FHIR_string import FHIR_string

# Raw data describing a biological sequence.
FHIR_MolecularSequence_StructureVariant = TypedDict(
    "FHIR_MolecularSequence_StructureVariant",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Information about chromosome structure variation DNA change type.
        "variantType": FHIR_CodeableConcept,
        # Used to indicate if the outer and inner start-end values have the same meaning.
        "exact": FHIR_boolean,
        # Extensions for exact
        "_exact": FHIR_Element,
        # Length of the variant chromosome.
        "length": FHIR_integer,
        # Extensions for length
        "_length": FHIR_Element,
        # Structural variant outer.
        "outer": FHIR_MolecularSequence_Outer,
        # Structural variant inner.
        "inner": FHIR_MolecularSequence_Inner,
    },
    total=False,
)
