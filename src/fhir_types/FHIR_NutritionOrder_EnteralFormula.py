from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_NutritionOrder_Administration import FHIR_NutritionOrder_Administration
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string

# A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
FHIR_NutritionOrder_EnteralFormula = TypedDict(
    "FHIR_NutritionOrder_EnteralFormula",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The type of enteral or infant formula such as an adult standard formula with fiber or a soy-based infant formula.
        "baseFormulaType": FHIR_CodeableConcept,
        # The product or brand name of the enteral or infant formula product such as "ACME Adult Standard Formula".
        "baseFormulaProductName": FHIR_string,
        # Extensions for baseFormulaProductName
        "_baseFormulaProductName": FHIR_Element,
        # Indicates the type of modular component such as protein, carbohydrate, fat or fiber to be provided in addition to or mixed with the base formula.
        "additiveType": FHIR_CodeableConcept,
        # The product or brand name of the type of modular component to be added to the formula.
        "additiveProductName": FHIR_string,
        # Extensions for additiveProductName
        "_additiveProductName": FHIR_Element,
        # The amount of energy (calories) that the formula should provide per specified volume, typically per mL or fluid oz.  For example, an infant may require a formula that provides 24 calories per fluid ounce or an adult may require an enteral formula that provides 1.5 calorie/mL.
        "caloricDensity": FHIR_Quantity,
        # The route or physiological path of administration into the patient's gastrointestinal  tract for purposes of providing the formula feeding, e.g. nasogastric tube.
        "routeofAdministration": FHIR_CodeableConcept,
        # Formula administration instructions as structured data.  This repeating structure allows for changing the administration rate or volume over time for both bolus and continuous feeding.  An example of this would be an instruction to increase the rate of continuous feeding every 2 hours.
        "administration": List[FHIR_NutritionOrder_Administration],
        # The maximum total quantity of formula that may be administered to a subject over the period of time, e.g. 1440 mL over 24 hours.
        "maxVolumeToDeliver": FHIR_Quantity,
        # Free text formula administration, feeding instructions or additional instructions or information.
        "administrationInstruction": FHIR_string,
        # Extensions for administrationInstruction
        "_administrationInstruction": FHIR_Element,
    },
    total=False,
)
