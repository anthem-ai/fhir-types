from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_string import FHIR_string

# This resource provides the adjudication details from the processing of a Claim resource.
FHIR_ClaimResponse_Error = TypedDict(
    "FHIR_ClaimResponse_Error",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The sequence number of the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structure.
        "itemSequence": FHIR_positiveInt,
        # Extensions for itemSequence
        "_itemSequence": FHIR_Element,
        # The sequence number of the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structure.
        "detailSequence": FHIR_positiveInt,
        # Extensions for detailSequence
        "_detailSequence": FHIR_Element,
        # The sequence number of the sub-detail within the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structure.
        "subDetailSequence": FHIR_positiveInt,
        # Extensions for subDetailSequence
        "_subDetailSequence": FHIR_Element,
        # An error code, from a specified code system, which details why the claim could not be adjudicated.
        "code": FHIR_CodeableConcept,
    },
    total=False,
)
