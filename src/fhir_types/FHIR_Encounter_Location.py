from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
FHIR_Encounter_Location = TypedDict(
    "FHIR_Encounter_Location",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The location where the encounter takes place.
        "location": FHIR_Reference,
        # The status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/time.
        "status": Literal["planned", "active", "reserved", "completed"],
        # Extensions for status
        "_status": FHIR_Element,
        # This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or query.
        "physicalType": FHIR_CodeableConcept,
        # Time period during which the patient was present at the location.
        "period": FHIR_Period,
    },
    total=False,
)