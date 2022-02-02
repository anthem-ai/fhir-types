from typing import Any, List, Literal, TypedDict

from .FHIR_Bundle_Link import FHIR_Bundle_Link
from .FHIR_Bundle_Request import FHIR_Bundle_Request
from .FHIR_Bundle_Response import FHIR_Bundle_Response
from .FHIR_Bundle_Search import FHIR_Bundle_Search
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A container for a collection of resources.
FHIR_Bundle_Entry = TypedDict(
    "FHIR_Bundle_Entry",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A series of links that provide context to this entry.
        "link": List[FHIR_Bundle_Link],
        # The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: * fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)* Results from operations might involve resources that are not identified.
        "fullUrl": FHIR_uri,
        # Extensions for fullUrl
        "_fullUrl": FHIR_Element,
        # The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.
        "resource": Any,
        # Information about the search process that lead to the creation of this entry.
        "search": FHIR_Bundle_Search,
        # Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.
        "request": FHIR_Bundle_Request,
        # Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.
        "response": FHIR_Bundle_Response,
    },
    total=False,
)
