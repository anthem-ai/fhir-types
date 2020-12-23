from typing import Any, List, Literal, TypedDict

from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
FHIR_Questionnaire_EnableWhen = TypedDict(
    "FHIR_Questionnaire_EnableWhen",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The linkId for the question whose answer (or lack of answer) governs whether this item is enabled.
        "question": FHIR_string,
        # Extensions for question
        "_question": FHIR_Element,
        # Specifies the criteria by which the question is enabled.
        "operator": Literal["exists", "=", "!=", ">", "<", ">=", "<="],
        # Extensions for operator
        "_operator": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerBoolean": bool,
        # Extensions for answerBoolean
        "_answerBoolean": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerDecimal": float,
        # Extensions for answerDecimal
        "_answerDecimal": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerInteger": float,
        # Extensions for answerInteger
        "_answerInteger": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerDate": str,
        # Extensions for answerDate
        "_answerDate": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerDateTime": str,
        # Extensions for answerDateTime
        "_answerDateTime": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerTime": str,
        # Extensions for answerTime
        "_answerTime": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerString": str,
        # Extensions for answerString
        "_answerString": FHIR_Element,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerCoding": FHIR_Coding,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerQuantity": FHIR_Quantity,
        # A value that the referenced question is tested using the specified operator in order for the item to be enabled.
        "answerReference": FHIR_Reference,
    },
    total=False,
)
