from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Property = TypedDict(
    "FHIR_SubstanceSpecification_Property",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A category for this property, e.g. Physical, Chemical, Enzymatic.
        "category": FHIR_CodeableConcept,
        # Property type e.g. viscosity, pH, isoelectric point.
        "code": FHIR_CodeableConcept,
        # Parameters that were used in the measurement of a property (e.g. for viscosity: measured at 20C with a pH of 7.1).
        "parameters": FHIR_string,
        # Extensions for parameters
        "_parameters": FHIR_Element,
        # A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol).
        "definingSubstanceReference": FHIR_Reference,
        # A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol).
        "definingSubstanceCodeableConcept": FHIR_CodeableConcept,
        # Quantitative value for this property.
        "amountQuantity": FHIR_Quantity,
        # Quantitative value for this property.
        "amountString": str,
        # Extensions for amountString
        "_amountString": FHIR_Element,
    },
    total=False,
)
