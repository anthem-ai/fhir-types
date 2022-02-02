from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri
from .FHIR_ValueSet_Designation import FHIR_ValueSet_Designation

# A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
FHIR_ValueSet_Contains = TypedDict(
    "FHIR_ValueSet_Contains",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An absolute URI which is the code system in which the code for this item in the expansion is defined.
        "system": FHIR_uri,
        # Extensions for system
        "_system": FHIR_Element,
        # If true, this entry is included in the expansion for navigational purposes, and the user cannot select the code directly as a proper value.
        "abstract": FHIR_boolean,
        # Extensions for abstract
        "_abstract": FHIR_Element,
        # If the concept is inactive in the code system that defines it. Inactive codes are those that are no longer to be used, but are maintained by the code system for understanding legacy data. It might not be known or specified whether an concept is inactive (and it may depend on the context of use).
        "inactive": FHIR_boolean,
        # Extensions for inactive
        "_inactive": FHIR_Element,
        # The version of the code system from this code was taken. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.
        "version": FHIR_string,
        # Extensions for version
        "_version": FHIR_Element,
        # The code for this item in the expansion hierarchy. If this code is missing the entry in the hierarchy is a place holder (abstract) and does not represent a valid code in the value set.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # The recommended display for this item in the expansion.
        "display": FHIR_string,
        # Extensions for display
        "_display": FHIR_Element,
        # Additional representations for this item - other languages, aliases, specialized purposes, used for particular purposes, etc. These are relevant when the conditions of the expansion do not fix to a single correct representation.
        "designation": List[FHIR_ValueSet_Designation],
        # Other codes and entries contained under this entry in the hierarchy.
        "contains": List[Any],
    },
    total=False,
)
