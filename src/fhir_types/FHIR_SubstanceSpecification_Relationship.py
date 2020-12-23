from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Relationship = TypedDict(
    "FHIR_SubstanceSpecification_Relationship",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A pointer to another substance, as a resource or just a representational code.
        "substanceReference": FHIR_Reference,
        # A pointer to another substance, as a resource or just a representational code.
        "substanceCodeableConcept": FHIR_CodeableConcept,
        # For example "salt to parent", "active moiety", "starting material".
        "relationship": FHIR_CodeableConcept,
        # For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible substance relationships.
        "isDefining": FHIR_boolean,
        # Extensions for isDefining
        "_isDefining": FHIR_Element,
        # A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other.
        "amountQuantity": FHIR_Quantity,
        # A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other.
        "amountRange": FHIR_Range,
        # A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other.
        "amountRatio": FHIR_Ratio,
        # A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other.
        "amountString": str,
        # Extensions for amountString
        "_amountString": FHIR_Element,
        # For use when the numeric.
        "amountRatioLowLimit": FHIR_Ratio,
        # An operator for the amount, for example "average", "approximately", "less than".
        "amountType": FHIR_CodeableConcept,
        # Supporting literature.
        "source": List[FHIR_Reference],
    },
    total=False,
)
