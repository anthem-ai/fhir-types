from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_MarketingStatus import FHIR_MarketingStatus
from .FHIR_MedicinalProduct_ManufacturingBusinessOperation import (
    FHIR_MedicinalProduct_ManufacturingBusinessOperation,
)
from .FHIR_MedicinalProduct_Name import FHIR_MedicinalProduct_Name
from .FHIR_MedicinalProduct_SpecialDesignation import (
    FHIR_MedicinalProduct_SpecialDesignation,
)
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
FHIR_MedicinalProduct = TypedDict(
    "FHIR_MedicinalProduct",
    {
        # This is a MedicinalProduct resource
        "resourceType": Literal["MedicinalProduct"],
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
        # Business identifier for this product. Could be an MPID.
        "identifier": List[FHIR_Identifier],
        # Regulatory type, e.g. Investigational or Authorized.
        "type": FHIR_CodeableConcept,
        # If this medicine applies to human or veterinary uses.
        "domain": FHIR_Coding,
        # The dose form for a single part product, or combined form of a multiple part product.
        "combinedPharmaceuticalDoseForm": FHIR_CodeableConcept,
        # The legal status of supply of the medicinal product as classified by the regulator.
        "legalStatusOfSupply": FHIR_CodeableConcept,
        # Whether the Medicinal Product is subject to additional monitoring for regulatory reasons.
        "additionalMonitoringIndicator": FHIR_CodeableConcept,
        # Whether the Medicinal Product is subject to special measures for regulatory reasons.
        "specialMeasures": List[FHIR_string],
        # Extensions for specialMeasures
        "_specialMeasures": List[FHIR_Element],
        # If authorised for use in children.
        "paediatricUseIndicator": FHIR_CodeableConcept,
        # Allows the product to be classified by various systems.
        "productClassification": List[FHIR_CodeableConcept],
        # Marketing status of the medicinal product, in contrast to marketing authorizaton.
        "marketingStatus": List[FHIR_MarketingStatus],
        # Pharmaceutical aspects of product.
        "pharmaceuticalProduct": List[FHIR_Reference],
        # Package representation for the product.
        "packagedMedicinalProduct": List[FHIR_Reference],
        # Supporting documentation, typically for regulatory submission.
        "attachedDocument": List[FHIR_Reference],
        # A master file for to the medicinal product (e.g. Pharmacovigilance System Master File).
        "masterFile": List[FHIR_Reference],
        # A product specific contact, person (in a role), or an organization.
        "contact": List[FHIR_Reference],
        # Clinical trials or studies that this product is involved in.
        "clinicalTrial": List[FHIR_Reference],
        # The product's name, including full name and possibly coded parts.
        "name": List[FHIR_MedicinalProduct_Name],
        # Reference to another product, e.g. for linking authorised to investigational product.
        "crossReference": List[FHIR_Identifier],
        # An operation applied to the product, for manufacturing or adminsitrative purpose.
        "manufacturingBusinessOperation": List[
            FHIR_MedicinalProduct_ManufacturingBusinessOperation
        ],
        # Indicates if the medicinal product has an orphan designation for the treatment of a rare disease.
        "specialDesignation": List[FHIR_MedicinalProduct_SpecialDesignation],
    },
    total=False,
)
