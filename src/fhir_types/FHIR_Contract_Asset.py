from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Contract_Answer import FHIR_Contract_Answer
from .FHIR_Contract_Context import FHIR_Contract_Context
from .FHIR_Contract_ValuedItem import FHIR_Contract_ValuedItem
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_Asset = TypedDict(
    "FHIR_Contract_Asset",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Differentiates the kind of the asset .
        "scope": FHIR_CodeableConcept,
        # Target entity type about which the term may be concerned.
        "type": List[FHIR_CodeableConcept],
        # Associated entities.
        "typeReference": List[FHIR_Reference],
        # May be a subtype or part of an offered asset.
        "subtype": List[FHIR_CodeableConcept],
        # Specifies the applicability of the term to an asset resource instance, and instances it refers to orinstances that refer to it, and/or are owned by the offeree.
        "relationship": FHIR_Coding,
        # Circumstance of the asset.
        "context": List[FHIR_Contract_Context],
        # Description of the quality and completeness of the asset that imay be a factor in its valuation.
        "condition": FHIR_string,
        # Extensions for condition
        "_condition": FHIR_Element,
        # Type of Asset availability for use or ownership.
        "periodType": List[FHIR_CodeableConcept],
        # Asset relevant contractual time period.
        "period": List[FHIR_Period],
        # Time period of asset use.
        "usePeriod": List[FHIR_Period],
        # Clause or question text (Prose Object) concerning the asset in a linked form, such as a QuestionnaireResponse used in the formation of the contract.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # Id [identifier??] of the clause or question text about the asset in the referenced form or QuestionnaireResponse.
        "linkId": List[FHIR_string],
        # Extensions for linkId
        "_linkId": List[FHIR_Element],
        # Response to assets.
        "answer": List[FHIR_Contract_Answer],
        # Security labels that protects the asset.
        "securityLabelNumber": List[FHIR_unsignedInt],
        # Extensions for securityLabelNumber
        "_securityLabelNumber": List[FHIR_Element],
        # Contract Valued Item List.
        "valuedItem": List[FHIR_Contract_ValuedItem],
    },
    total=False,
)
