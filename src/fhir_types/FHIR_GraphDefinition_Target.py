from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_GraphDefinition_Compartment import FHIR_GraphDefinition_Compartment
from .FHIR_string import FHIR_string

# A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
FHIR_GraphDefinition_Target = TypedDict(
    "FHIR_GraphDefinition_Target",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Type of resource this link refers to.
        "type": FHIR_code,
        # Extensions for type
        "_type": FHIR_Element,
        # A set of parameters to look up.
        "params": FHIR_string,
        # Extensions for params
        "_params": FHIR_Element,
        # Profile for the target resource.
        "profile": FHIR_canonical,
        # Compartment Consistency Rules.
        "compartment": List[FHIR_GraphDefinition_Compartment],
        # Additional links from target resource.
        "link": List[Any],
    },
    total=False,
)
