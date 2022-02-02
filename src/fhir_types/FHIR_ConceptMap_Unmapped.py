from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
FHIR_ConceptMap_Unmapped = TypedDict(
    "FHIR_ConceptMap_Unmapped",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Defines which action to take if there is no match for the source concept in the target system designated for the group. One of 3 actions are possible: use the unmapped code (this is useful when doing a mapping between versions, and only a few codes have changed), use a fixed code (a default code), or alternatively, a reference to a different concept map can be provided (by canonical URL).
        "mode": Literal["provided", "fixed", "other-map"],
        # Extensions for mode
        "_mode": FHIR_Element,
        # The fixed code to use when the mode = 'fixed'  - all unmapped codes are mapped to a single fixed code.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # The display for the code. The display is only provided to help editors when editing the concept map.
        "display": FHIR_string,
        # Extensions for display
        "_display": FHIR_Element,
        # The canonical reference to an additional ConceptMap resource instance to use for mapping if this ConceptMap resource contains no matching mapping for the source concept.
        "url": FHIR_canonical,
    },
    total=False,
)
