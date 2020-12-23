from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
FHIR_ImplementationGuide_Page = TypedDict(
    "FHIR_ImplementationGuide_Page",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The source address for the page.
        "nameUrl": str,
        # Extensions for nameUrl
        "_nameUrl": FHIR_Element,
        # The source address for the page.
        "nameReference": FHIR_Reference,
        # A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # A code that indicates how the page is generated.
        "generation": Literal["html", "markdown", "xml", "generated"],
        # Extensions for generation
        "_generation": FHIR_Element,
        # Nested Pages/Sections under this page.
        "page": List[Any],
    },
    total=False,
)