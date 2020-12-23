from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A duration of time during which an organism (or a process) has existed.
FHIR_Age = TypedDict(
    "FHIR_Age",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The value of the measured amount. The value includes an implicit precision in the presentation of the value.
        "value": FHIR_decimal,
        # Extensions for value
        "_value": FHIR_Element,
        # How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.
        "comparator": Literal["<", "<=", ">=", ">"],
        # Extensions for comparator
        "_comparator": FHIR_Element,
        # A human-readable form of the unit.
        "unit": FHIR_string,
        # Extensions for unit
        "_unit": FHIR_Element,
        # The identification of the system that provides the coded form of the unit.
        "system": FHIR_uri,
        # Extensions for system
        "_system": FHIR_Element,
        # A computer processable form of the unit in some unit representation system.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
    },
    total=False,
)
