from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Money import FHIR_Money
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
FHIR_Contract_ValuedItem = TypedDict(
    "FHIR_Contract_ValuedItem",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Specific type of Contract Valued Item that may be priced.
        "entityCodeableConcept": FHIR_CodeableConcept,
        # Specific type of Contract Valued Item that may be priced.
        "entityReference": FHIR_Reference,
        # Identifies a Contract Valued Item instance.
        "identifier": FHIR_Identifier,
        # Indicates the time during which this Contract ValuedItem information is effective.
        "effectiveTime": FHIR_dateTime,
        # Extensions for effectiveTime
        "_effectiveTime": FHIR_Element,
        # Specifies the units by which the Contract Valued Item is measured or counted, and quantifies the countable or measurable Contract Valued Item instances.
        "quantity": FHIR_Quantity,
        # A Contract Valued Item unit valuation measure.
        "unitPrice": FHIR_Money,
        # A real number that represents a multiplier used in determining the overall value of the Contract Valued Item delivered. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amount.
        "factor": FHIR_decimal,
        # Extensions for factor
        "_factor": FHIR_Element,
        # An amount that expresses the weighting (based on difficulty, cost and/or resource intensiveness) associated with the Contract Valued Item delivered. The concept of Points allows for assignment of point values for a Contract Valued Item, such that a monetary amount can be assigned to each point.
        "points": FHIR_decimal,
        # Extensions for points
        "_points": FHIR_Element,
        # Expresses the product of the Contract Valued Item unitQuantity and the unitPriceAmt. For example, the formula: unit Quantity * unit Price (Cost per Point) * factor Number  * points = net Amount. Quantity, factor and points are assumed to be 1 if not supplied.
        "net": FHIR_Money,
        # Terms of valuation.
        "payment": FHIR_string,
        # Extensions for payment
        "_payment": FHIR_Element,
        # When payment is due.
        "paymentDate": FHIR_dateTime,
        # Extensions for paymentDate
        "_paymentDate": FHIR_Element,
        # Who will make payment.
        "responsible": FHIR_Reference,
        # Who will receive payment.
        "recipient": FHIR_Reference,
        # Id  of the clause or question text related to the context of this valuedItem in the referenced form or QuestionnaireResponse.
        "linkId": List[FHIR_string],
        # Extensions for linkId
        "_linkId": List[FHIR_Element],
        # A set of security labels that define which terms are controlled by this condition.
        "securityLabelNumber": List[FHIR_unsignedInt],
        # Extensions for securityLabelNumber
        "_securityLabelNumber": List[FHIR_Element],
    },
    total=False,
)
