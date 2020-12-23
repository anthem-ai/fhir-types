from typing import Any, List, Literal, TypedDict

from .FHIR_base64Binary import FHIR_base64Binary
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
FHIR_Device_UdiCarrier = TypedDict(
    "FHIR_Device_UdiCarrier",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The device identifier (DI) is a mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device.
        "deviceIdentifier": FHIR_string,
        # Extensions for deviceIdentifier
        "_deviceIdentifier": FHIR_Element,
        # Organization that is charged with issuing UDIs for devices.  For example, the US FDA issuers include :1) GS1: http://hl7.org/fhir/NamingSystem/gs1-di, 2) HIBCC:http://hl7.org/fhir/NamingSystem/hibcc-dI, 3) ICCBBA for blood containers:http://hl7.org/fhir/NamingSystem/iccbba-blood-di, 4) ICCBA for other devices:http://hl7.org/fhir/NamingSystem/iccbba-other-di.
        "issuer": FHIR_uri,
        # Extensions for issuer
        "_issuer": FHIR_Element,
        # The identity of the authoritative source for UDI generation within a  jurisdiction.  All UDIs are globally unique within a single namespace with the appropriate repository uri as the system.  For example,  UDIs of devices managed in the U.S. by the FDA, the value is  http://hl7.org/fhir/NamingSystem/fda-udi.
        "jurisdiction": FHIR_uri,
        # Extensions for jurisdiction
        "_jurisdiction": FHIR_Element,
        # The full UDI carrier of the Automatic Identification and Data Capture (AIDC) technology representation of the barcode string as printed on the packaging of the device - e.g., a barcode or RFID.   Because of limitations on character sets in XML and the need to round-trip JSON data through XML, AIDC Formats *SHALL* be base64 encoded.
        "carrierAIDC": FHIR_base64Binary,
        # Extensions for carrierAIDC
        "_carrierAIDC": FHIR_Element,
        # The full UDI carrier as the human readable form (HRF) representation of the barcode string as printed on the packaging of the device.
        "carrierHRF": FHIR_string,
        # Extensions for carrierHRF
        "_carrierHRF": FHIR_Element,
        # A coded entry to indicate how the data was entered.
        "entryType": Literal[
            "barcode", "rfid", "manual", "card", "self-reported", "unknown"
        ],
        # Extensions for entryType
        "_entryType": FHIR_Element,
    },
    total=False,
)
