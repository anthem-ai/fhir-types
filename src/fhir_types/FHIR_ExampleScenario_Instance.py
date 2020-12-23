from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_ExampleScenario_ContainedInstance import (
    FHIR_ExampleScenario_ContainedInstance,
)
from .FHIR_ExampleScenario_Version import FHIR_ExampleScenario_Version
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# Example of workflow instance.
FHIR_ExampleScenario_Instance = TypedDict(
    "FHIR_ExampleScenario_Instance",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The id of the resource for referencing.
        "resourceId": FHIR_string,
        # Extensions for resourceId
        "_resourceId": FHIR_Element,
        # The type of the resource.
        "resourceType": FHIR_code,
        # Extensions for resourceType
        "_resourceType": FHIR_Element,
        # A short name for the resource instance.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Human-friendly description of the resource instance.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # A specific version of the resource.
        "version": List[FHIR_ExampleScenario_Version],
        # Resources contained in the instance (e.g. the observations contained in a bundle).
        "containedInstance": List[FHIR_ExampleScenario_ContainedInstance],
    },
    total=False,
)
