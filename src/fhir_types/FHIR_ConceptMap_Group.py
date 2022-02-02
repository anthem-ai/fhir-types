from typing import Any, List, Literal, TypedDict

from .FHIR_ConceptMap_Element import FHIR_ConceptMap_Element
from .FHIR_ConceptMap_Unmapped import FHIR_ConceptMap_Unmapped
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
FHIR_ConceptMap_Group = TypedDict(
    "FHIR_ConceptMap_Group",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # An absolute URI that identifies the source system where the concepts to be mapped are defined.
        "source": FHIR_uri,
        # Extensions for source
        "_source": FHIR_Element,
        # The specific version of the code system, as determined by the code system authority.
        "sourceVersion": FHIR_string,
        # Extensions for sourceVersion
        "_sourceVersion": FHIR_Element,
        # An absolute URI that identifies the target system that the concepts will be mapped to.
        "target": FHIR_uri,
        # Extensions for target
        "_target": FHIR_Element,
        # The specific version of the code system, as determined by the code system authority.
        "targetVersion": FHIR_string,
        # Extensions for targetVersion
        "_targetVersion": FHIR_Element,
        # Mappings for an individual concept in the source to one or more concepts in the target.
        "element": List[FHIR_ConceptMap_Element],
        # What to do when there is no mapping for the source concept. "Unmapped" does not include codes that are unmatched, and the unmapped element is ignored in a code is specified to have equivalence = unmatched.
        "unmapped": FHIR_ConceptMap_Unmapped,
    },
    total=False,
)
