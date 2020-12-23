from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
FHIR_ExplanationOfBenefit_Procedure = TypedDict(
    "FHIR_ExplanationOfBenefit_Procedure",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify procedure entries.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # When the condition was observed or the relative ranking.
        "type": List[FHIR_CodeableConcept],
        # Date and optionally time the procedure was performed.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The code or reference to a Procedure resource which identifies the clinical intervention performed.
        "procedureCodeableConcept": FHIR_CodeableConcept,
        # The code or reference to a Procedure resource which identifies the clinical intervention performed.
        "procedureReference": FHIR_Reference,
        # Unique Device Identifiers associated with this line item.
        "udi": List[FHIR_Reference],
    },
    total=False,
)
