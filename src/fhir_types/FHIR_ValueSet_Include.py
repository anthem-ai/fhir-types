from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_ValueSet_Concept import FHIR_ValueSet_Concept
from .FHIR_ValueSet_Filter import FHIR_ValueSet_Filter

# A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
FHIR_ValueSet_Include = TypedDict(
    "FHIR_ValueSet_Include",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An absolute URI which is the code system from which the selected codes come from.
        "system": FHIR_uri,
        # Extensions for system
        "_system": FHIR_Element,
        # The version of the code system that the codes are selected from, or the special version '*' for all versions.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # Specifies a concept to be included or excluded.
        "concept": List[FHIR_ValueSet_Concept],
        # Select concepts by specify a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified, they SHALL all be true.
        "filter": List[FHIR_ValueSet_Filter],
        # Selects the concepts found in this value set (based on its value set definition). This is an absolute URI that is a reference to ValueSet.url.  If multiple value sets are specified this includes the union of the contents of all of the referenced value sets.
        "valueSet": List[FHIR_canonical],
    },
    total=False,
)
