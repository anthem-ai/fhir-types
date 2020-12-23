from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Observation_ReferenceRange import FHIR_Observation_ReferenceRange
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_SampledData import FHIR_SampledData
from .FHIR_string import FHIR_string

# Measurements and simple assertions made about a patient, device or other subject.
FHIR_Observation_Component = TypedDict(
    "FHIR_Observation_Component",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Describes what was observed. Sometimes this is called the observation "code".
        "code": FHIR_CodeableConcept,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueQuantity": FHIR_Quantity,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueRange": FHIR_Range,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueRatio": FHIR_Ratio,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueSampledData": FHIR_SampledData,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The information determined as a result of making the observation, if the information has a simple value.
        "valuePeriod": FHIR_Period,
        # Provides a reason why the expected value in the element Observation.component.value[x] is missing.
        "dataAbsentReason": FHIR_CodeableConcept,
        # A categorical assessment of an observation value.  For example, high, low, normal.
        "interpretation": List[FHIR_CodeableConcept],
        # Guidance on how to interpret the value by comparison to a normal or recommended range.
        "referenceRange": List[FHIR_Observation_ReferenceRange],
    },
    total=False,
)
