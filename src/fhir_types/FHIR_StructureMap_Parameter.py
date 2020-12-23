from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A Map of relationships between 2 structures that can be used to transform data.
FHIR_StructureMap_Parameter = TypedDict(
    "FHIR_StructureMap_Parameter",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Parameter value - variable or literal.
        "valueId": str,
        # Extensions for valueId
        "_valueId": FHIR_Element,
        # Parameter value - variable or literal.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # Parameter value - variable or literal.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # Parameter value - variable or literal.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # Parameter value - variable or literal.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
    },
    total=False,
)
