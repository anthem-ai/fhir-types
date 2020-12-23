from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_ProdCharacteristic import FHIR_ProdCharacteristic
from .FHIR_ProductShelfLife import FHIR_ProductShelfLife
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A medicinal product in a container or package.
FHIR_MedicinalProductPackaged_PackageItem = TypedDict(
    "FHIR_MedicinalProductPackaged_PackageItem",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Including possibly Data Carrier Identifier.
        "identifier": List[FHIR_Identifier],
        # The physical type of the container of the medicine.
        "type": FHIR_CodeableConcept,
        # The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1.
        "quantity": FHIR_Quantity,
        # Material type of the package item.
        "material": List[FHIR_CodeableConcept],
        # A possible alternate material for the packaging.
        "alternateMaterial": List[FHIR_CodeableConcept],
        # A device accompanying a medicinal product.
        "device": List[FHIR_Reference],
        # The manufactured item as contained in the packaged medicinal product.
        "manufacturedItem": List[FHIR_Reference],
        # Allows containers within containers.
        "packageItem": List[Any],
        # Dimensions, color etc.
        "physicalCharacteristics": FHIR_ProdCharacteristic,
        # Other codeable characteristics.
        "otherCharacteristics": List[FHIR_CodeableConcept],
        # Shelf Life and storage information.
        "shelfLifeStorage": List[FHIR_ProductShelfLife],
        # Manufacturer of this Package Item.
        "manufacturer": List[FHIR_Reference],
    },
    total=False,
)
