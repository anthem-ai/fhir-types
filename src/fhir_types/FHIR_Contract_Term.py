from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Contract_Action import FHIR_Contract_Action
from .FHIR_Contract_Asset import FHIR_Contract_Asset
from .FHIR_Contract_Offer import FHIR_Contract_Offer
from .FHIR_Contract_SecurityLabel import FHIR_Contract_SecurityLabel
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_Term = TypedDict(
    "FHIR_Contract_Term",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Unique identifier for this particular Contract Provision.
        "identifier": FHIR_Identifier,
        # When this Contract Provision was issued.
        "issued": FHIR_dateTime,
        # Extensions for issued
        "_issued": FHIR_Element,
        # Relevant time or time-period when this Contract Provision is applicable.
        "applies": FHIR_Period,
        # The entity that the term applies to.
        "topicCodeableConcept": FHIR_CodeableConcept,
        # The entity that the term applies to.
        "topicReference": FHIR_Reference,
        # A legal clause or condition contained within a contract that requires one or both parties to perform a particular requirement by some specified time or prevents one or both parties from performing a particular requirement by some specified time.
        "type": FHIR_CodeableConcept,
        # A specialized legal clause or condition based on overarching contract type.
        "subType": FHIR_CodeableConcept,
        # Statement of a provision in a policy or a contract.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # Security labels that protect the handling of information about the term and its elements, which may be specifically identified..
        "securityLabel": List[FHIR_Contract_SecurityLabel],
        # The matter of concern in the context of this provision of the agrement.
        "offer": FHIR_Contract_Offer,
        # Contract Term Asset List.
        "asset": List[FHIR_Contract_Asset],
        # An actor taking a role in an activity for which it can be assigned some degree of responsibility for the activity taking place.
        "action": List[FHIR_Contract_Action],
        # Nested group of Contract Provisions.
        "group": List[Any],
    },
    total=False,
)
