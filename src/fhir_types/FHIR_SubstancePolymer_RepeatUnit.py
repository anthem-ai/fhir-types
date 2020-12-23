from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_SubstanceAmount import FHIR_SubstanceAmount
from .FHIR_SubstancePolymer_DegreeOfPolymerisation import (
    FHIR_SubstancePolymer_DegreeOfPolymerisation,
)
from .FHIR_SubstancePolymer_StructuralRepresentation import (
    FHIR_SubstancePolymer_StructuralRepresentation,
)

# Todo.
FHIR_SubstancePolymer_RepeatUnit = TypedDict(
    "FHIR_SubstancePolymer_RepeatUnit",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Todo.
        "orientationOfPolymerisation": FHIR_CodeableConcept,
        # Todo.
        "repeatUnit": FHIR_string,
        # Extensions for repeatUnit
        "_repeatUnit": FHIR_Element,
        # Todo.
        "amount": FHIR_SubstanceAmount,
        # Todo.
        "degreeOfPolymerisation": List[FHIR_SubstancePolymer_DegreeOfPolymerisation],
        # Todo.
        "structuralRepresentation": List[
            FHIR_SubstancePolymer_StructuralRepresentation
        ],
    },
    total=False,
)
