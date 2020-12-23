from typing import Any, List, Literal, TypedDict

from .FHIR_ClaimResponse_Adjudication import FHIR_ClaimResponse_Adjudication
from .FHIR_ClaimResponse_Detail import FHIR_ClaimResponse_Detail
from .FHIR_Element import FHIR_Element
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_string import FHIR_string

# This resource provides the adjudication details from the processing of a Claim resource.
FHIR_ClaimResponse_Item = TypedDict(
    "FHIR_ClaimResponse_Item",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely reference the claim item entries.
        "itemSequence": FHIR_positiveInt,
        # Extensions for itemSequence
        "_itemSequence": FHIR_Element,
        # The numbers associated with notes below which apply to the adjudication of this item.
        "noteNumber": List[FHIR_positiveInt],
        # Extensions for noteNumber
        "_noteNumber": List[FHIR_Element],
        # If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.
        "adjudication": List[FHIR_ClaimResponse_Adjudication],
        # A claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple items.
        "detail": List[FHIR_ClaimResponse_Detail],
    },
    total=False,
)
