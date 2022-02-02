from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim_CareTeam = TypedDict(
    "FHIR_Claim_CareTeam",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify care team entries.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # Member of the team who provided the product or service.
        "provider": FHIR_Reference,
        # The party who is billing and/or responsible for the claimed products or services.
        "responsible": FHIR_boolean,
        # Extensions for responsible
        "_responsible": FHIR_Element,
        # The lead, assisting or supervising practitioner and their discipline if a multidisciplinary team.
        "role": FHIR_CodeableConcept,
        # The qualification of the practitioner which is applicable for this service.
        "qualification": FHIR_CodeableConcept,
    },
    total=False,
)
