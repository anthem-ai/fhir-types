from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_positiveInt import FHIR_positiveInt
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
FHIR_Claim_SupportingInfo = TypedDict(
    "FHIR_Claim_SupportingInfo",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A number to uniquely identify supporting information entries.
        "sequence": FHIR_positiveInt,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # The general class of the information supplied: information; exception; accident, employment; onset, etc.
        "category": FHIR_CodeableConcept,
        # System and code pertaining to the specific information regarding special conditions relating to the setting, treatment or patient  for which care is sought.
        "code": FHIR_CodeableConcept,
        # The date when or period to which this information refers.
        "timingDate": str,
        # Extensions for timingDate
        "_timingDate": FHIR_Element,
        # The date when or period to which this information refers.
        "timingPeriod": FHIR_Period,
        # Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the data.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the data.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the data.
        "valueQuantity": FHIR_Quantity,
        # Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the data.
        "valueAttachment": FHIR_Attachment,
        # Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the data.
        "valueReference": FHIR_Reference,
        # Provides the reason in the situation where a reason code is required in addition to the content.
        "reason": FHIR_CodeableConcept,
    },
    total=False,
)
