from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
FHIR_CodeSystem_Property1 = TypedDict(
    "FHIR_CodeSystem_Property1",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A code that is a reference to CodeSystem.property.code.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # The value of this property.
        "valueCode": str,
        # Extensions for valueCode
        "_valueCode": FHIR_Element,
        # The value of this property.
        "valueCoding": FHIR_Coding,
        # The value of this property.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The value of this property.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The value of this property.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The value of this property.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The value of this property.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
    },
    total=False,
)
