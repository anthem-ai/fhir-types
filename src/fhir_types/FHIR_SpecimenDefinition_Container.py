from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_SpecimenDefinition_Additive import FHIR_SpecimenDefinition_Additive
from .FHIR_string import FHIR_string

# A kind of specimen with associated set of requirements.
FHIR_SpecimenDefinition_Container = TypedDict(
    "FHIR_SpecimenDefinition_Container",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The type of material of the container.
        "material": FHIR_CodeableConcept,
        # The type of container used to contain this kind of specimen.
        "type": FHIR_CodeableConcept,
        # Color of container cap.
        "cap": FHIR_CodeableConcept,
        # The textual description of the kind of container.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The capacity (volume or other measure) of this kind of container.
        "capacity": FHIR_Quantity,
        # The minimum volume to be conditioned in the container.
        "minimumVolumeQuantity": FHIR_Quantity,
        # The minimum volume to be conditioned in the container.
        "minimumVolumeString": str,
        # Extensions for minimumVolumeString
        "_minimumVolumeString": FHIR_Element,
        # Substance introduced in the kind of container to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.
        "additive": List[FHIR_SpecimenDefinition_Additive],
        # Special processing that should be applied to the container for this kind of specimen.
        "preparation": FHIR_string,
        # Extensions for preparation
        "_preparation": FHIR_Element,
    },
    total=False,
)
