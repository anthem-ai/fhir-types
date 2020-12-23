from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeSystem_Designation import FHIR_CodeSystem_Designation
from .FHIR_CodeSystem_Property1 import FHIR_CodeSystem_Property1
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string

# The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
FHIR_CodeSystem_Concept = TypedDict(
    "FHIR_CodeSystem_Concept",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A code - a text symbol - that uniquely identifies the concept within the code system.
        "code": FHIR_code,
        # Extensions for code
        "_code": FHIR_Element,
        # A human readable string that is the recommended default way to present this concept to a user.
        "display": FHIR_string,
        # Extensions for display
        "_display": FHIR_Element,
        # The formal definition of the concept. The code system resource does not make formal definitions required, because of the prevalence of legacy systems. However, they are highly recommended, as without them there is no formal meaning associated with the concept.
        "definition": FHIR_string,
        # Extensions for definition
        "_definition": FHIR_Element,
        # Additional representations for the concept - other languages, aliases, specialized purposes, used for particular purposes, etc.
        "designation": List[FHIR_CodeSystem_Designation],
        # A property value for this concept.
        "property": List[FHIR_CodeSystem_Property1],
        # Defines children of a concept to produce a hierarchy of concepts. The nature of the relationships is variable (is-a/contains/categorizes) - see hierarchyMeaning.
        "concept": List[Any],
    },
    total=False,
)
