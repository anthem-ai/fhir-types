from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
FHIR_ProdCharacteristic = TypedDict(
    "FHIR_ProdCharacteristic",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Where applicable, the height can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "height": FHIR_Quantity,
        # Where applicable, the width can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "width": FHIR_Quantity,
        # Where applicable, the depth can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "depth": FHIR_Quantity,
        # Where applicable, the weight can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "weight": FHIR_Quantity,
        # Where applicable, the nominal volume can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "nominalVolume": FHIR_Quantity,
        # Where applicable, the external diameter can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.
        "externalDiameter": FHIR_Quantity,
        # Where applicable, the shape can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.
        "shape": FHIR_string,
        # Extensions for shape
        "_shape": FHIR_Element,
        # Where applicable, the color can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.
        "color": List[FHIR_string],
        # Extensions for color
        "_color": List[FHIR_Element],
        # Where applicable, the imprint can be specified as text.
        "imprint": List[FHIR_string],
        # Extensions for imprint
        "_imprint": List[FHIR_Element],
        # Where applicable, the image can be provided The format of the image attachment shall be specified by regional implementations.
        "image": List[FHIR_Attachment],
        # Where applicable, the scoring can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.
        "scoring": FHIR_CodeableConcept,
    },
    total=False,
)
