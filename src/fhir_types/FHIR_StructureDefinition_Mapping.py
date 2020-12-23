from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.
FHIR_StructureDefinition_Mapping = TypedDict(
    "FHIR_StructureDefinition_Mapping",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An Internal id that is used to identify this mapping set when specific mappings are made.
        "identity": FHIR_id,
        # Extensions for identity
        "_identity": FHIR_Element,
        # An absolute URI that identifies the specification that this mapping is expressed to.
        "uri": FHIR_uri,
        # Extensions for uri
        "_uri": FHIR_Element,
        # A name for the specification that is being mapped to.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Comments about this mapping, including version notes, issues, scope limitations, and other important notes for usage.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
    },
    total=False,
)
