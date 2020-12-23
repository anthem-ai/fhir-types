from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_MeasureReport_Component import FHIR_MeasureReport_Component
from .FHIR_MeasureReport_Population1 import FHIR_MeasureReport_Population1
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
FHIR_MeasureReport_Stratum = TypedDict(
    "FHIR_MeasureReport_Stratum",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The value for this stratum, expressed as a CodeableConcept. When defining stratifiers on complex values, the value must be rendered such that the value for each stratum within the stratifier is unique.
        "value": FHIR_CodeableConcept,
        # A stratifier component value.
        "component": List[FHIR_MeasureReport_Component],
        # The populations that make up the stratum, one for each type of population appropriate to the measure.
        "population": List[FHIR_MeasureReport_Population1],
        # The measure score for this stratum, calculated as appropriate for the measure type and scoring method, and based on only the members of this stratum.
        "measureScore": FHIR_Quantity,
    },
    total=False,
)
