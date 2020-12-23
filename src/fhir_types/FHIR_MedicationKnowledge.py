from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_markdown import FHIR_markdown
from .FHIR_MedicationKnowledge_AdministrationGuidelines import (
    FHIR_MedicationKnowledge_AdministrationGuidelines,
)
from .FHIR_MedicationKnowledge_Cost import FHIR_MedicationKnowledge_Cost
from .FHIR_MedicationKnowledge_DrugCharacteristic import (
    FHIR_MedicationKnowledge_DrugCharacteristic,
)
from .FHIR_MedicationKnowledge_Ingredient import FHIR_MedicationKnowledge_Ingredient
from .FHIR_MedicationKnowledge_Kinetics import FHIR_MedicationKnowledge_Kinetics
from .FHIR_MedicationKnowledge_MedicineClassification import (
    FHIR_MedicationKnowledge_MedicineClassification,
)
from .FHIR_MedicationKnowledge_MonitoringProgram import (
    FHIR_MedicationKnowledge_MonitoringProgram,
)
from .FHIR_MedicationKnowledge_Monograph import FHIR_MedicationKnowledge_Monograph
from .FHIR_MedicationKnowledge_Packaging import FHIR_MedicationKnowledge_Packaging
from .FHIR_MedicationKnowledge_Regulatory import FHIR_MedicationKnowledge_Regulatory
from .FHIR_MedicationKnowledge_RelatedMedicationKnowledge import (
    FHIR_MedicationKnowledge_RelatedMedicationKnowledge,
)
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Information about a medication that is used to support knowledge.
FHIR_MedicationKnowledge = TypedDict(
    "FHIR_MedicationKnowledge",
    {
        # This is a MedicationKnowledge resource
        "resourceType": Literal["MedicationKnowledge"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A code that specifies this medication, or a textual description if no code is available. Usage note: This could be a standard medication code such as a code from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local formulary code, optionally with translations to other code systems.
        "code": FHIR_CodeableConcept,
        # A code to indicate if the medication is in active use.  The status refers to the validity about the information of the medication and not to its medicinal properties.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Describes the details of the manufacturer of the medication product.  This is not intended to represent the distributor of a medication product.
        "manufacturer": FHIR_Reference,
        # Describes the form of the item.  Powder; tablets; capsule.
        "doseForm": FHIR_CodeableConcept,
        # Specific amount of the drug in the packaged product.  For example, when specifying a product that has the same strength (For example, Insulin glargine 100 unit per mL solution for injection), this attribute provides additional clarification of the package amount (For example, 3 mL, 10mL, etc.).
        "amount": FHIR_Quantity,
        # Additional names for a medication, for example, the name(s) given to a medication in different countries.  For example, acetaminophen and paracetamol or salbutamol and albuterol.
        "synonym": List[FHIR_string],
        # Extensions for synonym
        "_synonym": List[FHIR_Element],
        # Associated or related knowledge about a medication.
        "relatedMedicationKnowledge": List[
            FHIR_MedicationKnowledge_RelatedMedicationKnowledge
        ],
        # Associated or related medications.  For example, if the medication is a branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g. Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this would link to a branded product (e.g. Crestor).
        "associatedMedication": List[FHIR_Reference],
        # Category of the medication or product (e.g. branded product, therapeutic moeity, generic product, innovator product, etc.).
        "productType": List[FHIR_CodeableConcept],
        # Associated documentation about the medication.
        "monograph": List[FHIR_MedicationKnowledge_Monograph],
        # Identifies a particular constituent of interest in the product.
        "ingredient": List[FHIR_MedicationKnowledge_Ingredient],
        # The instructions for preparing the medication.
        "preparationInstruction": FHIR_markdown,
        # Extensions for preparationInstruction
        "_preparationInstruction": FHIR_Element,
        # The intended or approved route of administration.
        "intendedRoute": List[FHIR_CodeableConcept],
        # The price of the medication.
        "cost": List[FHIR_MedicationKnowledge_Cost],
        # The program under which the medication is reviewed.
        "monitoringProgram": List[FHIR_MedicationKnowledge_MonitoringProgram],
        # Guidelines for the administration of the medication.
        "administrationGuidelines": List[
            FHIR_MedicationKnowledge_AdministrationGuidelines
        ],
        # Categorization of the medication within a formulary or classification system.
        "medicineClassification": List[FHIR_MedicationKnowledge_MedicineClassification],
        # Information that only applies to packages (not products).
        "packaging": FHIR_MedicationKnowledge_Packaging,
        # Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.
        "drugCharacteristic": List[FHIR_MedicationKnowledge_DrugCharacteristic],
        # Potential clinical issue with or between medication(s) (for example, drug-drug interaction, drug-disease contraindication, drug-allergy interaction, etc.).
        "contraindication": List[FHIR_Reference],
        # Regulatory information about a medication.
        "regulatory": List[FHIR_MedicationKnowledge_Regulatory],
        # The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.
        "kinetics": List[FHIR_MedicationKnowledge_Kinetics],
    },
    total=False,
)
