from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string

# A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
FHIR_CapabilityStatement_Document = TypedDict(
    "FHIR_CapabilityStatement_Document",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Mode of this document declaration - whether an application is a producer or consumer.
        "mode": Literal["producer", "consumer"],
        # Extensions for mode
        "_mode": FHIR_Element,
        # A description of how the application supports or uses the specified document profile.  For example, when documents are created, what action is taken with consumed documents, etc.
        "documentation": FHIR_markdown,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # A profile on the document Bundle that constrains which resources are present, and their contents.
        "profile": FHIR_canonical,
    },
    total=False,
)
