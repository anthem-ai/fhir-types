from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_string import FHIR_string

# The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
FHIR_RiskEvidenceSynthesis_CertaintySubcomponent = TypedDict(
    "FHIR_RiskEvidenceSynthesis_CertaintySubcomponent",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Type of subcomponent of certainty rating.
        "type": FHIR_CodeableConcept,
        # A rating of a subcomponent of rating certainty.
        "rating": List[FHIR_CodeableConcept],
        # A human-readable string to clarify or explain concepts about the resource.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
