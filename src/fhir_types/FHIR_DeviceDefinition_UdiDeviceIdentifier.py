from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# The characteristics, operational status and capabilities of a medical-related component of a medical device.
FHIR_DeviceDefinition_UdiDeviceIdentifier = TypedDict(
    "FHIR_DeviceDefinition_UdiDeviceIdentifier",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier.
        "deviceIdentifier": FHIR_string,
        # Extensions for deviceIdentifier
        "_deviceIdentifier": FHIR_Element,
        # The organization that assigns the identifier algorithm.
        "issuer": FHIR_uri,
        # Extensions for issuer
        "_issuer": FHIR_Element,
        # The jurisdiction to which the deviceIdentifier applies.
        "jurisdiction": FHIR_uri,
        # Extensions for jurisdiction
        "_jurisdiction": FHIR_Element,
    },
    total=False,
)
