from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string
from .FHIR_StructureMap_Parameter import FHIR_StructureMap_Parameter

# A Map of relationships between 2 structures that can be used to transform data.
FHIR_StructureMap_Target = TypedDict(
    "FHIR_StructureMap_Target",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Type or variable this rule applies to.
        "context": FHIR_id,
        # Extensions for context
        "_context": FHIR_Element,
        # How to interpret the context.
        "contextType": Literal["type", "variable"],
        # Extensions for contextType
        "_contextType": FHIR_Element,
        # Field to create in the context.
        "element": FHIR_string,
        # Extensions for element
        "_element": FHIR_Element,
        # Named context for field, if desired, and a field is specified.
        "variable": FHIR_id,
        # Extensions for variable
        "_variable": FHIR_Element,
        # If field is a list, how to manage the list.
        "listMode": List[Literal["first", "share", "last", "collate"]],
        # Extensions for listMode
        "_listMode": List[FHIR_Element],
        # Internal rule reference for shared list items.
        "listRuleId": FHIR_id,
        # Extensions for listRuleId
        "_listRuleId": FHIR_Element,
        # How the data is copied / created.
        "transform": Literal[
            "create",
            "copy",
            "truncate",
            "escape",
            "cast",
            "append",
            "translate",
            "reference",
            "dateOp",
            "uuid",
            "pointer",
            "evaluate",
            "cc",
            "c",
            "qty",
            "id",
            "cp",
        ],
        # Extensions for transform
        "_transform": FHIR_Element,
        # Parameters to the transform.
        "parameter": List[FHIR_StructureMap_Parameter],
    },
    total=False,
)
