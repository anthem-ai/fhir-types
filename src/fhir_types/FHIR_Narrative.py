from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_xhtml import FHIR_xhtml

# A human-readable summary of the resource conveying the essential clinical and business information for the resource.
FHIR_Narrative = TypedDict(
    "FHIR_Narrative",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The status of the narrative - whether it's entirely generated (from just the defined data or the extensions too), or whether a human authored it and it may contain additional data.
        "status": Literal["generated", "extensions", "additional", "empty"],
        # Extensions for status
        "_status": FHIR_Element,
        # The actual narrative content, a stripped down version of XHTML.
        "div": FHIR_xhtml,
    },
    total=False,
)
