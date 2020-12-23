from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_string import FHIR_string

# The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
FHIR_EffectEvidenceSynthesis_SampleSize = TypedDict(
    "FHIR_EffectEvidenceSynthesis_SampleSize",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Human-readable summary of sample size.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Number of studies included in this evidence synthesis.
        "numberOfStudies": FHIR_integer,
        # Extensions for numberOfStudies
        "_numberOfStudies": FHIR_Element,
        # Number of participants included in this evidence synthesis.
        "numberOfParticipants": FHIR_integer,
        # Extensions for numberOfParticipants
        "_numberOfParticipants": FHIR_Element,
    },
    total=False,
)
