from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_ExampleScenario_ContainedInstance import (
    FHIR_ExampleScenario_ContainedInstance,
)
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# Example of workflow instance.
FHIR_ExampleScenario_Operation = TypedDict(
    "FHIR_ExampleScenario_Operation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The sequential number of the interaction, e.g. 1.2.5.
        "number": FHIR_string,
        # Extensions for number
        "_number": FHIR_Element,
        # The type of operation - CRUD.
        "type": FHIR_string,
        # Extensions for type
        "_type": FHIR_Element,
        # The human-friendly name of the interaction.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Who starts the transaction.
        "initiator": FHIR_string,
        # Extensions for initiator
        "_initiator": FHIR_Element,
        # Who receives the transaction.
        "receiver": FHIR_string,
        # Extensions for receiver
        "_receiver": FHIR_Element,
        # A comment to be inserted in the diagram.
        "description": FHIR_markdown,
        # Extensions for description
        "_description": FHIR_Element,
        # Whether the initiator is deactivated right after the transaction.
        "initiatorActive": FHIR_boolean,
        # Extensions for initiatorActive
        "_initiatorActive": FHIR_Element,
        # Whether the receiver is deactivated right after the transaction.
        "receiverActive": FHIR_boolean,
        # Extensions for receiverActive
        "_receiverActive": FHIR_Element,
        # Each resource instance used by the initiator.
        "request": FHIR_ExampleScenario_ContainedInstance,
        # Each resource instance used by the responder.
        "response": FHIR_ExampleScenario_ContainedInstance,
    },
    total=False,
)
