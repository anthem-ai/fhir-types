from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_OperationDefinition_Binding import FHIR_OperationDefinition_Binding
from .FHIR_OperationDefinition_ReferencedFrom import (
    FHIR_OperationDefinition_ReferencedFrom,
)
from .FHIR_string import FHIR_string

# A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
FHIR_OperationDefinition_Parameter = TypedDict(
    "FHIR_OperationDefinition_Parameter",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The name of used to identify the parameter.
        "name": FHIR_code,
        # Extensions for name
        "_name": FHIR_Element,
        # Whether this is an input or an output parameter.
        "use": Literal["in", "out"],
        # Extensions for use
        "_use": FHIR_Element,
        # The minimum number of times this parameter SHALL appear in the request or response.
        "min": FHIR_integer,
        # Extensions for min
        "_min": FHIR_Element,
        # The maximum number of times this element is permitted to appear in the request or response.
        "max": FHIR_string,
        # Extensions for max
        "_max": FHIR_Element,
        # Describes the meaning or use of this parameter.
        "documentation": FHIR_string,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # The type for this parameter.
        "type": FHIR_code,
        # Extensions for type
        "_type": FHIR_Element,
        # Used when the type is "Reference" or "canonical", and identifies a profile structure or implementation Guide that applies to the target of the reference this parameter refers to. If any profiles are specified, then the content must conform to at least one of them. The URL can be a local reference - to a contained StructureDefinition, or a reference to another StructureDefinition or Implementation Guide by a canonical URL. When an implementation guide is specified, the target resource SHALL conform to at least one profile defined in the implementation guide.
        "targetProfile": List[FHIR_canonical],
        # How the parameter is understood as a search parameter. This is only used if the parameter type is 'string'.
        "searchType": Literal[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
            "special",
        ],
        # Extensions for searchType
        "_searchType": FHIR_Element,
        # Binds to a value set if this parameter is coded (code, Coding, CodeableConcept).
        "binding": FHIR_OperationDefinition_Binding,
        # Identifies other resource parameters within the operation invocation that are expected to resolve to this resource.
        "referencedFrom": List[FHIR_OperationDefinition_ReferencedFrom],
        # The parts of a nested Parameter.
        "part": List[Any],
    },
    total=False,
)
