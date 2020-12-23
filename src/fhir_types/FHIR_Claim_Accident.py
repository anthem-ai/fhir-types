from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim_Accident = TypedDict(
    "FHIR_Claim_Accident",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Date of an accident event  related to the products and services contained in the claim.
        "date": FHIR_date,
        # Extensions for date
        "_date": FHIR_Element,
        # The type or context of the accident event for the purposes of selection of potential insurance coverages and determination of coordination between insurers.
        "type": FHIR_CodeableConcept,
        # The physical location of the accident event.
        "locationAddress": FHIR_Address,
        # The physical location of the accident event.
        "locationReference": FHIR_Reference,
    },
    total=False,
)
