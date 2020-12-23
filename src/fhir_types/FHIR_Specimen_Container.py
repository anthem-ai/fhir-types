from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A sample to be used for analysis.
FHIR_Specimen_Container = TypedDict(
    "FHIR_Specimen_Container",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Id for container. There may be multiple; a manufacturer's bar code, lab assigned identifier, etc. The container ID may differ from the specimen id in some circumstances.
        "identifier": List[FHIR_Identifier],
        # Textual description of the container.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The type of container associated with the specimen (e.g. slide, aliquot, etc.).
        "type": FHIR_CodeableConcept,
        # The capacity (volume or other measure) the container may contain.
        "capacity": FHIR_Quantity,
        # The quantity of specimen in the container; may be volume, dimensions, or other appropriate measurements, depending on the specimen type.
        "specimenQuantity": FHIR_Quantity,
        # Introduced substance to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.
        "additiveCodeableConcept": FHIR_CodeableConcept,
        # Introduced substance to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.
        "additiveReference": FHIR_Reference,
    },
    total=False,
)
