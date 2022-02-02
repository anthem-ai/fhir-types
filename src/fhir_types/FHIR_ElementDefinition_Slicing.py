from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_ElementDefinition_Discriminator import FHIR_ElementDefinition_Discriminator
from .FHIR_string import FHIR_string

# Captures constraints on each element within the resource, profile, or extension.
FHIR_ElementDefinition_Slicing = TypedDict(
    "FHIR_ElementDefinition_Slicing",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Designates which child elements are used to discriminate between the slices when processing an instance. If one or more discriminators are provided, the value of the child elements in the instance data SHALL completely distinguish which slice the element in the resource matches based on the allowed values for those elements in each of the slices.
        "discriminator": List[FHIR_ElementDefinition_Discriminator],
        # A human-readable text description of how the slicing works. If there is no discriminator, this is required to be present to provide whatever information is possible about how the slices can be differentiated.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # If the matching elements have to occur in the same order as defined in the profile.
        "ordered": FHIR_boolean,
        # Extensions for ordered
        "_ordered": FHIR_Element,
        # Whether additional slices are allowed or not. When the slices are ordered, profile authors can also say that additional slices are only allowed at the end.
        "rules": Literal["closed", "open", "openAtEnd"],
        # Extensions for rules
        "_rules": FHIR_Element,
    },
    total=False,
)
