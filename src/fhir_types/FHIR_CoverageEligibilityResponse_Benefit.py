from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Money import FHIR_Money
from .FHIR_string import FHIR_string

# This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
FHIR_CoverageEligibilityResponse_Benefit = TypedDict(
    "FHIR_CoverageEligibilityResponse_Benefit",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Classification of benefit being provided.
        "type": FHIR_CodeableConcept,
        # The quantity of the benefit which is permitted under the coverage.
        "allowedUnsignedInt": float,
        # Extensions for allowedUnsignedInt
        "_allowedUnsignedInt": FHIR_Element,
        # The quantity of the benefit which is permitted under the coverage.
        "allowedString": str,
        # Extensions for allowedString
        "_allowedString": FHIR_Element,
        # The quantity of the benefit which is permitted under the coverage.
        "allowedMoney": FHIR_Money,
        # The quantity of the benefit which have been consumed to date.
        "usedUnsignedInt": float,
        # Extensions for usedUnsignedInt
        "_usedUnsignedInt": FHIR_Element,
        # The quantity of the benefit which have been consumed to date.
        "usedString": str,
        # Extensions for usedString
        "_usedString": FHIR_Element,
        # The quantity of the benefit which have been consumed to date.
        "usedMoney": FHIR_Money,
    },
    total=False,
)
