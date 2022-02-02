from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A sample to be used for analysis.
FHIR_Specimen_Processing = TypedDict(
    "FHIR_Specimen_Processing",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Textual description of procedure.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # A coded value specifying the procedure used to process the specimen.
        "procedure": FHIR_CodeableConcept,
        # Material used in the processing step.
        "additive": List[FHIR_Reference],
        # A record of the time or period when the specimen processing occurred.  For example the time of sample fixation or the period of time the sample was in formalin.
        "timeDateTime": str,
        # Extensions for timeDateTime
        "_timeDateTime": FHIR_Element,
        # A record of the time or period when the specimen processing occurred.  For example the time of sample fixation or the period of time the sample was in formalin.
        "timePeriod": FHIR_Period,
    },
    total=False,
)
