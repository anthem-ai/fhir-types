from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
FHIR_EffectEvidenceSynthesis_ResultsByExposure = TypedDict(
    "FHIR_EffectEvidenceSynthesis_ResultsByExposure",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Human-readable summary of results by exposure state.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Whether these results are for the exposure state or alternative exposure state.
        "exposureState": Literal["exposure", "exposure-alternative"],
        # Extensions for exposureState
        "_exposureState": FHIR_Element,
        # Used to define variant exposure states such as low-risk state.
        "variantState": FHIR_CodeableConcept,
        # Reference to a RiskEvidenceSynthesis resource.
        "riskEvidenceSynthesis": FHIR_Reference,
    },
    total=False,
)
