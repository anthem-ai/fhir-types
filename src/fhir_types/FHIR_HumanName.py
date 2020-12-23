from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string

# A human's name with the ability to identify parts and usage.
FHIR_HumanName = TypedDict(
    "FHIR_HumanName",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # Identifies the purpose for this name.
        "use": Literal[
            "usual", "official", "temp", "nickname", "anonymous", "old", "maiden"
        ],
        # Extensions for use
        "_use": FHIR_Element,
        # Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.
        "family": FHIR_string,
        # Extensions for family
        "_family": FHIR_Element,
        # Given name.
        "given": List[FHIR_string],
        # Extensions for given
        "_given": List[FHIR_Element],
        # Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name.
        "prefix": List[FHIR_string],
        # Extensions for prefix
        "_prefix": List[FHIR_Element],
        # Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name.
        "suffix": List[FHIR_string],
        # Extensions for suffix
        "_suffix": List[FHIR_Element],
        # Indicates the period of time when this name was valid for the named person.
        "period": FHIR_Period,
    },
    total=False,
)
