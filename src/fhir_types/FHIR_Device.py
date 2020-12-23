from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Device_DeviceName import FHIR_Device_DeviceName
from .FHIR_Device_Property import FHIR_Device_Property
from .FHIR_Device_Specialization import FHIR_Device_Specialization
from .FHIR_Device_UdiCarrier import FHIR_Device_UdiCarrier
from .FHIR_Device_Version import FHIR_Device_Version
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
FHIR_Device = TypedDict(
    "FHIR_Device",
    {
        # This is a Device resource
        "resourceType": Literal["Device"],
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
        # Unique instance identifiers assigned to a device by manufacturers other organizations or owners.
        "identifier": List[FHIR_Identifier],
        # The reference to the definition for the device.
        "definition": FHIR_Reference,
        # Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.
        "udiCarrier": List[FHIR_Device_UdiCarrier],
        # Status of the Device availability.
        "status": Literal["active", "inactive", "entered-in-error", "unknown"],
        # Extensions for status
        "_status": FHIR_Element,
        # Reason for the dtatus of the Device availability.
        "statusReason": List[FHIR_CodeableConcept],
        # The distinct identification string as required by regulation for a human cell, tissue, or cellular and tissue-based product.
        "distinctIdentifier": FHIR_string,
        # Extensions for distinctIdentifier
        "_distinctIdentifier": FHIR_Element,
        # A name of the manufacturer.
        "manufacturer": FHIR_string,
        # Extensions for manufacturer
        "_manufacturer": FHIR_Element,
        # The date and time when the device was manufactured.
        "manufactureDate": FHIR_dateTime,
        # Extensions for manufactureDate
        "_manufactureDate": FHIR_Element,
        # The date and time beyond which this device is no longer valid or should not be used (if applicable).
        "expirationDate": FHIR_dateTime,
        # Extensions for expirationDate
        "_expirationDate": FHIR_Element,
        # Lot number assigned by the manufacturer.
        "lotNumber": FHIR_string,
        # Extensions for lotNumber
        "_lotNumber": FHIR_Element,
        # The serial number assigned by the organization when the device was manufactured.
        "serialNumber": FHIR_string,
        # Extensions for serialNumber
        "_serialNumber": FHIR_Element,
        # This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.
        "deviceName": List[FHIR_Device_DeviceName],
        # The model number for the device.
        "modelNumber": FHIR_string,
        # Extensions for modelNumber
        "_modelNumber": FHIR_Element,
        # The part number of the device.
        "partNumber": FHIR_string,
        # Extensions for partNumber
        "_partNumber": FHIR_Element,
        # The kind or type of device.
        "type": FHIR_CodeableConcept,
        # The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.
        "specialization": List[FHIR_Device_Specialization],
        # The actual design of the device or software version running on the device.
        "version": List[FHIR_Device_Version],
        # The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.
        "property": List[FHIR_Device_Property],
        # Patient information, If the device is affixed to a person.
        "patient": FHIR_Reference,
        # An organization that is responsible for the provision and ongoing maintenance of the device.
        "owner": FHIR_Reference,
        # Contact details for an organization or a particular human that is responsible for the device.
        "contact": List[FHIR_ContactPoint],
        # The place where the device can be found.
        "location": FHIR_Reference,
        # A network address on which the device may be contacted directly.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # Descriptive information, usage information or implantation information that is not captured in an existing element.
        "note": List[FHIR_Annotation],
        # Provides additional safety characteristics about a medical device.  For example devices containing latex.
        "safety": List[FHIR_CodeableConcept],
        # The parent device.
        "parent": FHIR_Reference,
    },
    total=False,
)
