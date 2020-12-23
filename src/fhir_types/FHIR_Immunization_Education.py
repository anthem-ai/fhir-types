from typing import Any, List, Literal, TypedDict

from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
FHIR_Immunization_Education = TypedDict(
    "FHIR_Immunization_Education",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifier of the material presented to the patient.
        "documentType": FHIR_string,
        # Extensions for documentType
        "_documentType": FHIR_Element,
        # Reference pointer to the educational material given to the patient if the information was on line.
        "reference": FHIR_uri,
        # Extensions for reference
        "_reference": FHIR_Element,
        # Date the educational material was published.
        "publicationDate": FHIR_dateTime,
        # Extensions for publicationDate
        "_publicationDate": FHIR_Element,
        # Date the educational material was given to the patient.
        "presentationDate": FHIR_dateTime,
        # Extensions for presentationDate
        "_presentationDate": FHIR_Element,
    },
    total=False,
)
