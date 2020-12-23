from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_SubstanceSpecification_Official import FHIR_SubstanceSpecification_Official

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Name = TypedDict(
    "FHIR_SubstanceSpecification_Name",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The actual name.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Name type.
        "type": FHIR_CodeableConcept,
        # The status of the name.
        "status": FHIR_CodeableConcept,
        # If this is the preferred name for this substance.
        "preferred": FHIR_boolean,
        # Extensions for preferred
        "_preferred": FHIR_Element,
        # Language of the name.
        "language": List[FHIR_CodeableConcept],
        # The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive.
        "domain": List[FHIR_CodeableConcept],
        # The jurisdiction where this name applies.
        "jurisdiction": List[FHIR_CodeableConcept],
        # A synonym of this name.
        "synonym": List[Any],
        # A translation for this name.
        "translation": List[Any],
        # Details of the official nature of this name.
        "official": List[FHIR_SubstanceSpecification_Official],
        # Supporting literature.
        "source": List[FHIR_Reference],
    },
    total=False,
)
