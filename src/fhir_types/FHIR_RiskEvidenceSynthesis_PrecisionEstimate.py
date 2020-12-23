from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
FHIR_RiskEvidenceSynthesis_PrecisionEstimate = TypedDict(
    "FHIR_RiskEvidenceSynthesis_PrecisionEstimate",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Examples include confidence interval and interquartile range.
        "type": FHIR_CodeableConcept,
        # Use 95 for a 95% confidence interval.
        "level": FHIR_decimal,
        # Extensions for level
        "_level": FHIR_Element,
        # Lower bound of confidence interval.
        "from": FHIR_decimal,
        # Extensions for from
        "_from": FHIR_Element,
        # Upper bound of confidence interval.
        "to": FHIR_decimal,
        # Extensions for to
        "_to": FHIR_Element,
    },
    total=False,
)
