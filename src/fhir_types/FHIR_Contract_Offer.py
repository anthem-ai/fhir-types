from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Contract_Answer import FHIR_Contract_Answer
from .FHIR_Contract_Party import FHIR_Contract_Party
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_Offer = TypedDict(
    "FHIR_Contract_Offer",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Unique identifier for this particular Contract Provision.
        "identifier": List[FHIR_Identifier],
        # Offer Recipient.
        "party": List[FHIR_Contract_Party],
        # The owner of an asset has the residual control rights over the asset: the right to decide all usages of the asset in any way not inconsistent with a prior contract, custom, or law (Hart, 1995, p. 30).
        "topic": FHIR_Reference,
        # Type of Contract Provision such as specific requirements, purposes for actions, obligations, prohibitions, e.g. life time maximum benefit.
        "type": FHIR_CodeableConcept,
        # Type of choice made by accepting party with respect to an offer made by an offeror/ grantee.
        "decision": FHIR_CodeableConcept,
        # How the decision about a Contract was conveyed.
        "decisionMode": List[FHIR_CodeableConcept],
        # Response to offer text.
        "answer": List[FHIR_Contract_Answer],
        # Human readable form of this Contract Offer.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # The id of the clause or question text of the offer in the referenced questionnaire/response.
        "linkId": List[FHIR_string],
        # Extensions for linkId
        "_linkId": List[FHIR_Element],
        # Security labels that protects the offer.
        "securityLabelNumber": List[FHIR_unsignedInt],
        # Extensions for securityLabelNumber
        "_securityLabelNumber": List[FHIR_Element],
    },
    total=False,
)
