from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_markdown import FHIR_markdown
from .FHIR_string import FHIR_string
from .FHIR_url import FHIR_url

# Related artifacts such as additional documentation, justification, or bibliographic references.
FHIR_RelatedArtifact = TypedDict(
    "FHIR_RelatedArtifact",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The type of relationship to the related artifact.
        "type": Literal[
            "documentation",
            "justification",
            "citation",
            "predecessor",
            "successor",
            "derived-from",
            "depends-on",
            "composed-of",
        ],
        # Extensions for type
        "_type": FHIR_Element,
        # A short label that can be used to reference the citation from elsewhere in the containing artifact, such as a footnote index.
        "label": FHIR_string,
        # Extensions for label
        "_label": FHIR_Element,
        # A brief description of the document or knowledge resource being referenced, suitable for display to a consumer.
        "display": FHIR_string,
        # Extensions for display
        "_display": FHIR_Element,
        # A bibliographic citation for the related artifact. This text SHOULD be formatted according to an accepted citation format.
        "citation": FHIR_markdown,
        # Extensions for citation
        "_citation": FHIR_Element,
        # A url for the artifact that can be followed to access the actual content.
        "url": FHIR_url,
        # Extensions for url
        "_url": FHIR_Element,
        # The document being referenced, represented as an attachment. This is exclusive with the resource element.
        "document": FHIR_Attachment,
        # The related resource, such as a library, value set, profile, or other knowledge resource.
        "resource": FHIR_canonical,
    },
    total=False,
)
