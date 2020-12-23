from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_ExampleScenario_Step import FHIR_ExampleScenario_Step
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# Example of workflow instance.
FHIR_ExampleScenario_Alternative = TypedDict(
    "FHIR_ExampleScenario_Alternative",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The label to display for the alternative that gives a sense of the circumstance in which the alternative should be invoked.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # A human-readable description of the alternative explaining when the alternative should occur rather than the base step.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # What happens in each alternative option.
        "step": List[FHIR_ExampleScenario_Step],
    },
    total=False,
)
