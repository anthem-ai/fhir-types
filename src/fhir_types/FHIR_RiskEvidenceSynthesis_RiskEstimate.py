from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_RiskEvidenceSynthesis_PrecisionEstimate import (
    FHIR_RiskEvidenceSynthesis_PrecisionEstimate,
)
from .FHIR_string import FHIR_string

# The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
FHIR_RiskEvidenceSynthesis_RiskEstimate = TypedDict(
    "FHIR_RiskEvidenceSynthesis_RiskEstimate",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Human-readable summary of risk estimate.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Examples include proportion and mean.
        "type": FHIR_CodeableConcept,
        # The point estimate of the risk estimate.
        "value": FHIR_decimal,
        # Extensions for value
        "_value": FHIR_Element,
        # Specifies the UCUM unit for the outcome.
        "unitOfMeasure": FHIR_CodeableConcept,
        # The sample size for the group that was measured for this risk estimate.
        "denominatorCount": FHIR_integer,
        # Extensions for denominatorCount
        "_denominatorCount": FHIR_Element,
        # The number of group members with the outcome of interest.
        "numeratorCount": FHIR_integer,
        # Extensions for numeratorCount
        "_numeratorCount": FHIR_Element,
        # A description of the precision of the estimate for the effect.
        "precisionEstimate": List[FHIR_RiskEvidenceSynthesis_PrecisionEstimate],
    },
    total=False,
)
