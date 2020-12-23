from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# Information about a medication that is used to support knowledge.
FHIR_MedicationKnowledge_DrugCharacteristic = TypedDict(
    "FHIR_MedicationKnowledge_DrugCharacteristic",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A code specifying which characteristic of the medicine is being described (for example, colour, shape, imprint).
        "type": FHIR_CodeableConcept,
        # Description of the characteristic.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # Description of the characteristic.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # Description of the characteristic.
        "valueQuantity": FHIR_Quantity,
        # Description of the characteristic.
        "valueBase64Binary": str,
        # Extensions for valueBase64Binary
        "_valueBase64Binary": FHIR_Element,
    },
    total=False,
)