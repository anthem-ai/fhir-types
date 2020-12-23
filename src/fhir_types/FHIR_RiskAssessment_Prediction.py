from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Range import FHIR_Range
from .FHIR_string import FHIR_string

# An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
FHIR_RiskAssessment_Prediction = TypedDict(
    "FHIR_RiskAssessment_Prediction",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # One of the potential outcomes for the patient (e.g. remission, death,  a particular condition).
        "outcome": FHIR_CodeableConcept,
        # Indicates how likely the outcome is (in the specified timeframe).
        "probabilityDecimal": float,
        # Extensions for probabilityDecimal
        "_probabilityDecimal": FHIR_Element,
        # Indicates how likely the outcome is (in the specified timeframe).
        "probabilityRange": FHIR_Range,
        # Indicates how likely the outcome is (in the specified timeframe), expressed as a qualitative value (e.g. low, medium, or high).
        "qualitativeRisk": FHIR_CodeableConcept,
        # Indicates the risk for this particular subject (with their specific characteristics) divided by the risk of the population in general.  (Numbers greater than 1 = higher risk than the population, numbers less than 1 = lower risk.).
        "relativeRisk": FHIR_decimal,
        # Extensions for relativeRisk
        "_relativeRisk": FHIR_Element,
        # Indicates the period of time or age range of the subject to which the specified probability applies.
        "whenPeriod": FHIR_Period,
        # Indicates the period of time or age range of the subject to which the specified probability applies.
        "whenRange": FHIR_Range,
        # Additional information explaining the basis for the prediction.
        "rationale": FHIR_string,
        # Extensions for rationale
        "_rationale": FHIR_Element,
    },
    total=False,
)
