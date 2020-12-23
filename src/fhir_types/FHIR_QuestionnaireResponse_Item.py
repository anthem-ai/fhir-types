from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
FHIR_QuestionnaireResponse_Item = TypedDict(
    "FHIR_QuestionnaireResponse_Item",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The item from the Questionnaire that corresponds to this item in the QuestionnaireResponse resource.
        "linkId": FHIR_string,
        # Extensions for linkId
        "_linkId": FHIR_Element,
        # A reference to an [[[ElementDefinition]]] that provides the details for the item.
        "definition": FHIR_uri,
        # Extensions for definition
        "_definition": FHIR_Element,
        # Text that is displayed above the contents of the group or as the text of the question being answered.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # The respondent's answer(s) to the question.
        "answer": List[Any],
        # Questions or sub-groups nested beneath a question or group.
        "item": List[Any],
    },
    total=False,
)
