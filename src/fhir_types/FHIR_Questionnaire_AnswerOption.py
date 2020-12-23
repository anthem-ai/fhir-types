from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
FHIR_Questionnaire_AnswerOption = TypedDict(
    "FHIR_Questionnaire_AnswerOption",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A potential answer that's allowed as the answer to this question.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # A potential answer that's allowed as the answer to this question.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # A potential answer that's allowed as the answer to this question.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # A potential answer that's allowed as the answer to this question.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # A potential answer that's allowed as the answer to this question.
        "valueCoding": FHIR_Coding,
        # A potential answer that's allowed as the answer to this question.
        "valueReference": FHIR_Reference,
        # Indicates whether the answer value is selected when the list of possible answers is initially shown.
        "initialSelected": FHIR_boolean,
        # Extensions for initialSelected
        "_initialSelected": FHIR_Element,
    },
    total=False,
)
