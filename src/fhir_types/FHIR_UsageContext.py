from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
FHIR_UsageContext = TypedDict(
    "FHIR_UsageContext",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # A code that identifies the type of context being specified by this usage context.
        "code": FHIR_Coding,
        # A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.
        "valueQuantity": FHIR_Quantity,
        # A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.
        "valueRange": FHIR_Range,
        # A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.
        "valueReference": FHIR_Reference,
    },
    total=False,
)
