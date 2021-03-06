from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_DeviceDefinition_Capability import FHIR_DeviceDefinition_Capability
from .FHIR_DeviceDefinition_DeviceName import FHIR_DeviceDefinition_DeviceName
from .FHIR_DeviceDefinition_Material import FHIR_DeviceDefinition_Material
from .FHIR_DeviceDefinition_Property import FHIR_DeviceDefinition_Property
from .FHIR_DeviceDefinition_Specialization import FHIR_DeviceDefinition_Specialization
from .FHIR_DeviceDefinition_UdiDeviceIdentifier import (
    FHIR_DeviceDefinition_UdiDeviceIdentifier,
)
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_ProdCharacteristic import FHIR_ProdCharacteristic
from .FHIR_ProductShelfLife import FHIR_ProductShelfLife
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# The characteristics, operational status and capabilities of a medical-related component of a medical device.
FHIR_DeviceDefinition = TypedDict(
    "FHIR_DeviceDefinition",
    {
        # This is a DeviceDefinition resource
        "resourceType": Literal["DeviceDefinition"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Unique instance identifiers assigned to a device by the software, manufacturers, other organizations or owners. For example: handle ID.
        "identifier": List[FHIR_Identifier],
        # Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.
        "udiDeviceIdentifier": List[FHIR_DeviceDefinition_UdiDeviceIdentifier],
        # A name of the manufacturer.
        "manufacturerString": str,
        # Extensions for manufacturerString
        "_manufacturerString": FHIR_Element,
        # A name of the manufacturer.
        "manufacturerReference": FHIR_Reference,
        # A name given to the device to identify it.
        "deviceName": List[FHIR_DeviceDefinition_DeviceName],
        # The model number for the device.
        "modelNumber": FHIR_string,
        # Extensions for modelNumber
        "_modelNumber": FHIR_Element,
        # What kind of device or device system this is.
        "type": FHIR_CodeableConcept,
        # The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.
        "specialization": List[FHIR_DeviceDefinition_Specialization],
        # The available versions of the device, e.g., software versions.
        "version": List[FHIR_string],
        # Extensions for version
        "_version": List[FHIR_Element],
        # Safety characteristics of the device.
        "safety": List[FHIR_CodeableConcept],
        # Shelf Life and storage information.
        "shelfLifeStorage": List[FHIR_ProductShelfLife],
        # Dimensions, color etc.
        "physicalCharacteristics": FHIR_ProdCharacteristic,
        # Language code for the human-readable text strings produced by the device (all supported).
        "languageCode": List[FHIR_CodeableConcept],
        # Device capabilities.
        "capability": List[FHIR_DeviceDefinition_Capability],
        # The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.
        "property": List[FHIR_DeviceDefinition_Property],
        # An organization that is responsible for the provision and ongoing maintenance of the device.
        "owner": FHIR_Reference,
        # Contact details for an organization or a particular human that is responsible for the device.
        "contact": List[FHIR_ContactPoint],
        # A network address on which the device may be contacted directly.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # Access to on-line information about the device.
        "onlineInformation": FHIR_uri,
        # Extensions for onlineInformation
        "_onlineInformation": FHIR_Element,
        # Descriptive information, usage information or implantation information that is not captured in an existing element.
        "note": List[FHIR_Annotation],
        # The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product).
        "quantity": FHIR_Quantity,
        # The parent device it can be part of.
        "parentDevice": FHIR_Reference,
        # A substance used to create the material(s) of which the device is made.
        "material": List[FHIR_DeviceDefinition_Material],
    },
    total=False,
)
