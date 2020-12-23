from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
FHIR_Questionnaire_Initial = TypedDict(
    "FHIR_Questionnaire_Initial",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The actual value to for an initial answer.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The actual value to for an initial answer.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # The actual value to for an initial answer.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The actual value to for an initial answer.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # The actual value to for an initial answer.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The actual value to for an initial answer.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # The actual value to for an initial answer.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The actual value to for an initial answer.
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # The actual value to for an initial answer.
        "valueAttachment": FHIR_Attachment,
        # The actual value to for an initial answer.
        "valueCoding": FHIR_Coding,
        # The actual value to for an initial answer.
        "valueQuantity": FHIR_Quantity,
        # The actual value to for an initial answer.
        "valueReference": FHIR_Reference,
    },
    total=False,
)
