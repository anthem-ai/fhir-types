from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
FHIR_MedicinalProduct_SpecialDesignation = TypedDict(
    "FHIR_MedicinalProduct_SpecialDesignation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifier for the designation, or procedure number.
        "identifier": List[FHIR_Identifier],
        # The type of special designation, e.g. orphan drug, minor use.
        "type": FHIR_CodeableConcept,
        # The intended use of the product, e.g. prevention, treatment.
        "intendedUse": FHIR_CodeableConcept,
        # Condition for which the medicinal use applies.
        "indicationCodeableConcept": FHIR_CodeableConcept,
        # Condition for which the medicinal use applies.
        "indicationReference": FHIR_Reference,
        # For example granted, pending, expired or withdrawn.
        "status": FHIR_CodeableConcept,
        # Date when the designation was granted.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Animal species for which this applies.
        "species": FHIR_CodeableConcept,
    },
    total=False,
)
