from typing import Any, List, Literal, TypedDict

from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A  text note which also  contains information about who made the statement and when.
FHIR_Annotation = TypedDict(
    "FHIR_Annotation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The individual responsible for making the annotation.
        "authorReference": FHIR_Reference,
        # The individual responsible for making the annotation.
        "authorString": str,
        # Extensions for authorString
        "_authorString": FHIR_Element,
        # Indicates when this particular annotation was made.
        "time": FHIR_dateTime,
        # Extensions for time
        "_time": FHIR_Element,
        # The text of the annotation in markdown format.
        "text": FHIR_markdown,
        # Extensions for text
        "_text": FHIR_Element,
    },
    total=False,
)
