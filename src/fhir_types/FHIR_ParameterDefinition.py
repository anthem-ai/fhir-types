from typing import Any, List, Literal, TypedDict

from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_string import FHIR_string

# The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
FHIR_ParameterDefinition = TypedDict(
    "FHIR_ParameterDefinition",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The name of the parameter used to allow access to the value of the parameter in evaluation contexts.
        "name": FHIR_code,
        # Extensions for name
        "_name": FHIR_Element,
        # Whether the parameter is input or output for the module.
        "use": FHIR_code,
        # Extensions for use
        "_use": FHIR_Element,
        # The minimum number of times this parameter SHALL appear in the request or response.
        "min": FHIR_integer,
        # Extensions for min
        "_min": FHIR_Element,
        # The maximum number of times this element is permitted to appear in the request or response.
        "max": FHIR_string,
        # Extensions for max
        "_max": FHIR_Element,
        # A brief discussion of what the parameter is for and how it is used by the module.
        "documentation": FHIR_string,
        # Extensions for documentation
        "_documentation": FHIR_Element,
        # The type of the parameter.
        "type": FHIR_code,
        # Extensions for type
        "_type": FHIR_Element,
        # If specified, this indicates a profile that the input data must conform to, or that the output data will conform to.
        "profile": FHIR_canonical,
    },
    total=False,
)
