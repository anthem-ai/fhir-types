from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_ImplementationGuide_Page1 import FHIR_ImplementationGuide_Page1
from .FHIR_ImplementationGuide_Resource1 import FHIR_ImplementationGuide_Resource1
from .FHIR_string import FHIR_string
from .FHIR_url import FHIR_url

# A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
FHIR_ImplementationGuide_Manifest = TypedDict(
    "FHIR_ImplementationGuide_Manifest",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A pointer to official web page, PDF or other rendering of the implementation guide.
        "rendering": FHIR_url,
        # Extensions for rendering
        "_rendering": FHIR_Element,
        # A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.
        "resource": List[FHIR_ImplementationGuide_Resource1],
        # Information about a page within the IG.
        "page": List[FHIR_ImplementationGuide_Page1],
        # Indicates a relative path to an image that exists within the IG.
        "image": List[FHIR_string],
        # Extensions for image
        "_image": List[FHIR_Element],
        # Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.
        "other": List[FHIR_string],
        # Extensions for other
        "_other": List[FHIR_Element],
    },
    total=False,
)
