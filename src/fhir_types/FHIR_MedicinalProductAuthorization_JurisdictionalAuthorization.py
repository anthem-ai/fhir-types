from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string

# The regulatory authorization of a medicinal product.
FHIR_MedicinalProductAuthorization_JurisdictionalAuthorization = TypedDict(
    "FHIR_MedicinalProductAuthorization_JurisdictionalAuthorization",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The assigned number for the marketing authorization.
        "identifier": List[FHIR_Identifier],
        # Country of authorization.
        "country": FHIR_CodeableConcept,
        # Jurisdiction within a country.
        "jurisdiction": List[FHIR_CodeableConcept],
        # The legal status of supply in a jurisdiction or region.
        "legalStatusOfSupply": FHIR_CodeableConcept,
        # The start and expected end date of the authorization.
        "validityPeriod": FHIR_Period,
    },
    total=False,
)
