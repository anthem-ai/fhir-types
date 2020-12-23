from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_Coding import FHIR_Coding
from .FHIR_Element import FHIR_Element
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_QuestionnaireResponse_Item import FHIR_QuestionnaireResponse_Item
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
FHIR_QuestionnaireResponse_Answer = TypedDict(
    "FHIR_QuestionnaireResponse_Answer",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueAttachment": FHIR_Attachment,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueCoding": FHIR_Coding,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueQuantity": FHIR_Quantity,
        # The answer (or one of the answers) provided by the respondent to the question.
        "valueReference": FHIR_Reference,
        # Nested groups and/or questions found within this particular answer.
        "item": List[FHIR_QuestionnaireResponse_Item],
    },
    total=False,
)
