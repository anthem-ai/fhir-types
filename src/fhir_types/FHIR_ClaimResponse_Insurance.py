from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Element import FHIR_Element
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# This resource provides the adjudication details from the processing of a Claim resource.
FHIR_ClaimResponse_Insurance = TypedDict(
    "FHIR_ClaimResponse_Insurance",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit order.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # A flag to indicate that this Coverage is to be used for adjudication of this claim when set to true.
        "focal": FHIR_boolean,
        # Extensions for focal
        "_focal": FHIR_Element,
        # Reference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information system.
        "coverage": FHIR_Reference,
        # A business agreement number established between the provider and the insurer for special business processing purposes.
        "businessArrangement": FHIR_string,
        # Extensions for businessArrangement
        "_businessArrangement": FHIR_Element,
        # The result of the adjudication of the line items for the Coverage specified in this insurance.
        "claimResponse": FHIR_Reference,
    },
    total=False,
)
