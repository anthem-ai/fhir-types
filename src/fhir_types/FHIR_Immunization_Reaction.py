from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
FHIR_Immunization_Reaction = TypedDict(
    "FHIR_Immunization_Reaction",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Date of reaction to the immunization.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Details of the reaction.
        "detail": FHIR_Reference,
        # Self-reported indicator.
        "reported": FHIR_boolean,
        # Extensions for reported
        "_reported": FHIR_Element,
    },
    total=False,
)
