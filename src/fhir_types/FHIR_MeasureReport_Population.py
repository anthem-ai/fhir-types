from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
FHIR_MeasureReport_Population = TypedDict(
    "FHIR_MeasureReport_Population",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The type of the population.
        "code": FHIR_CodeableConcept,
        # The number of members of the population.
        "count": FHIR_integer,
        # Extensions for count
        "_count": FHIR_Element,
        # This element refers to a List of subject level MeasureReport resources, one for each subject in this population.
        "subjectResults": FHIR_Reference,
    },
    total=False,
)
