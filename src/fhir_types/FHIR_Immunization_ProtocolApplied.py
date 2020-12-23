from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
FHIR_Immunization_ProtocolApplied = TypedDict(
    "FHIR_Immunization_ProtocolApplied",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # One possible path to achieve presumed immunity against a disease - within the context of an authority.
        "series": FHIR_string,
        # Extensions for series
        "_series": FHIR_Element,
        # Indicates the authority who published the protocol (e.g. ACIP) that is being followed.
        "authority": FHIR_Reference,
        # The vaccine preventable disease the dose is being administered against.
        "targetDisease": List[FHIR_CodeableConcept],
        # Nominal position in a series.
        "doseNumberPositiveInt": float,
        # Extensions for doseNumberPositiveInt
        "_doseNumberPositiveInt": FHIR_Element,
        # Nominal position in a series.
        "doseNumberString": str,
        # Extensions for doseNumberString
        "_doseNumberString": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesPositiveInt": float,
        # Extensions for seriesDosesPositiveInt
        "_seriesDosesPositiveInt": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesString": str,
        # Extensions for seriesDosesString
        "_seriesDosesString": FHIR_Element,
    },
    total=False,
)
