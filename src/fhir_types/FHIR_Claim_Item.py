from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_Claim_Detail import FHIR_Claim_Detail
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_Money import FHIR_Money
from .FHIR_Period import FHIR_Period
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim_Item = TypedDict(
    "FHIR_Claim_Item",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify item entries.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # CareTeam members related to this service or product.
        "careTeamSequence": List[FHIR_positiveInt],
        # Extensions for careTeamSequence
        "_careTeamSequence": List[FHIR_Element],
        # Diagnosis applicable for this service or product.
        "diagnosisSequence": List[FHIR_positiveInt],
        # Extensions for diagnosisSequence
        "_diagnosisSequence": List[FHIR_Element],
        # Procedures applicable for this service or product.
        "procedureSequence": List[FHIR_positiveInt],
        # Extensions for procedureSequence
        "_procedureSequence": List[FHIR_Element],
        # Exceptions, special conditions and supporting information applicable for this service or product.
        "informationSequence": List[FHIR_positiveInt],
        # Extensions for informationSequence
        "_informationSequence": List[FHIR_Element],
        # The type of revenue or cost center providing the product and/or service.
        "revenue": FHIR_CodeableConcept,
        # Code to identify the general type of benefits under which products and services are provided.
        "category": FHIR_CodeableConcept,
        # When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the item.
        "productOrService": FHIR_CodeableConcept,
        # Item typification or modifiers codes to convey additional context for the product or service.
        "modifier": List[FHIR_CodeableConcept],
        # Identifies the program under which this may be recovered.
        "programCode": List[FHIR_CodeableConcept],
        # The date or dates when the service or product was supplied, performed or completed.
        "servicedDate": str,
        # Extensions for servicedDate
        "_servicedDate": FHIR_Element,
        # The date or dates when the service or product was supplied, performed or completed.
        "servicedPeriod": FHIR_Period,
        # Where the product or service was provided.
        "locationCodeableConcept": FHIR_CodeableConcept,
        # Where the product or service was provided.
        "locationAddress": FHIR_Address,
        # Where the product or service was provided.
        "locationReference": FHIR_Reference,
        # The number of repetitions of a service or product.
        "quantity": FHIR_Quantity,
        # If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the group.
        "unitPrice": FHIR_Money,
        # A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amount.
        "factor": FHIR_decimal,
        # Extensions for factor
        "_factor": FHIR_Element,
        # The quantity times the unit price for an additional service or product or charge.
        "net": FHIR_Money,
        # Unique Device Identifiers associated with this line item.
        "udi": List[FHIR_Reference],
        # Physical service site on the patient (limb, tooth, etc.).
        "bodySite": FHIR_CodeableConcept,
        # A region or surface of the bodySite, e.g. limb region or tooth surface(s).
        "subSite": List[FHIR_CodeableConcept],
        # The Encounters during which this Claim was created or to which the creation of this record is tightly associated.
        "encounter": List[FHIR_Reference],
        # A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.
        "detail": List[FHIR_Claim_Detail],
    },
    total=False,
)
