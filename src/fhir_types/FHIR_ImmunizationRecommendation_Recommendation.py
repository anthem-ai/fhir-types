from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_ImmunizationRecommendation_DateCriterion import (
    FHIR_ImmunizationRecommendation_DateCriterion,
)
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
FHIR_ImmunizationRecommendation_Recommendation = TypedDict(
    "FHIR_ImmunizationRecommendation_Recommendation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Vaccine(s) or vaccine group that pertain to the recommendation.
        "vaccineCode": List[FHIR_CodeableConcept],
        # The targeted disease for the recommendation.
        "targetDisease": FHIR_CodeableConcept,
        # Vaccine(s) which should not be used to fulfill the recommendation.
        "contraindicatedVaccineCode": List[FHIR_CodeableConcept],
        # Indicates the patient status with respect to the path to immunity for the target disease.
        "forecastStatus": FHIR_CodeableConcept,
        # The reason for the assigned forecast status.
        "forecastReason": List[FHIR_CodeableConcept],
        # Vaccine date recommendations.  For example, earliest date to administer, latest date to administer, etc.
        "dateCriterion": List[FHIR_ImmunizationRecommendation_DateCriterion],
        # Contains the description about the protocol under which the vaccine was administered.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # One possible path to achieve presumed immunity against a disease - within the context of an authority.
        "series": FHIR_string,
        # Extensions for series
        "_series": FHIR_Element,
        # Nominal position of the recommended dose in a series (e.g. dose 2 is the next recommended dose).
        "doseNumberPositiveInt": float,
        # Extensions for doseNumberPositiveInt
        "_doseNumberPositiveInt": FHIR_Element,
        # Nominal position of the recommended dose in a series (e.g. dose 2 is the next recommended dose).
        "doseNumberString": str,
        # Extensions for doseNumberString
        "_doseNumberString": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesPositiveInt": float,
        # Extensions for seriesDosesPositiveInt
        "_seriesDosesPositiveInt": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesString": str,
        # Extensions for seriesDosesString
        "_seriesDosesString": FHIR_Element,
        # Immunization event history and/or evaluation that supports the status and recommendation.
        "supportingImmunization": List[FHIR_Reference],
        # Patient Information that supports the status and recommendation.  This includes patient observations, adverse reactions and allergy/intolerance information.
        "supportingPatientInformation": List[FHIR_Reference],
    },
    total=False,
)
