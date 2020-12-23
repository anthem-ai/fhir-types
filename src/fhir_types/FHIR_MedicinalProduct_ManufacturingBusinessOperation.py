from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
FHIR_MedicinalProduct_ManufacturingBusinessOperation = TypedDict(
    "FHIR_MedicinalProduct_ManufacturingBusinessOperation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The type of manufacturing operation.
        "operationType": FHIR_CodeableConcept,
        # Regulatory authorization reference number.
        "authorisationReferenceNumber": FHIR_Identifier,
        # Regulatory authorization date.
        "effectiveDate": FHIR_dateTime,
        # Extensions for effectiveDate
        "_effectiveDate": FHIR_Element,
        # To indicate if this proces is commercially confidential.
        "confidentialityIndicator": FHIR_CodeableConcept,
        # The manufacturer or establishment associated with the process.
        "manufacturer": List[FHIR_Reference],
        # A regulator which oversees the operation.
        "regulator": FHIR_Reference,
    },
    total=False,
)
