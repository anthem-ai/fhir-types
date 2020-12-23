from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_TerminologyCapabilities_Filter import FHIR_TerminologyCapabilities_Filter

# A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
FHIR_TerminologyCapabilities_Version = TypedDict(
    "FHIR_TerminologyCapabilities_Version",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # For version-less code systems, there should be a single version with no identifier.
        "code": FHIR_string,
        # Extensions for code
        "_code": FHIR_Element,
        # If this is the default version for this code system.
        "isDefault": FHIR_boolean,
        # Extensions for isDefault
        "_isDefault": FHIR_Element,
        # If the compositional grammar defined by the code system is supported.
        "compositional": FHIR_boolean,
        # Extensions for compositional
        "_compositional": FHIR_Element,
        # Language Displays supported.
        "language": List[FHIR_code],
        # Extensions for language
        "_language": List[FHIR_Element],
        # Filter Properties supported.
        "filter": List[FHIR_TerminologyCapabilities_Filter],
        # Properties supported for $lookup.
        "property": List[FHIR_code],
        # Extensions for property
        "_property": List[FHIR_Element],
    },
    total=False,
)
