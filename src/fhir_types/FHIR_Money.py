from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# An amount of economic utility in some recognized currency.
FHIR_Money = TypedDict(
    "FHIR_Money",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # Numerical value (with implicit precision).
        "value": FHIR_decimal,
        # Extensions for value
        "_value": FHIR_Element,
        # ISO 4217 Currency Code.
        "currency": FHIR_code,
        # Extensions for currency
        "_currency": FHIR_Element,
    },
    total=False,
)
