from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_MedicinalProductAuthorization_JurisdictionalAuthorization import (
    FHIR_MedicinalProductAuthorization_JurisdictionalAuthorization,
)
from .FHIR_MedicinalProductAuthorization_Procedure import (
    FHIR_MedicinalProductAuthorization_Procedure,
)
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# The regulatory authorization of a medicinal product.
FHIR_MedicinalProductAuthorization = TypedDict(
    "FHIR_MedicinalProductAuthorization",
    {
        # This is a MedicinalProductAuthorization resource
        "resourceType": Literal["MedicinalProductAuthorization"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Business identifier for the marketing authorization, as assigned by a regulator.
        "identifier": List[FHIR_Identifier],
        # The medicinal product that is being authorized.
        "subject": FHIR_Reference,
        # The country in which the marketing authorization has been granted.
        "country": List[FHIR_CodeableConcept],
        # Jurisdiction within a country.
        "jurisdiction": List[FHIR_CodeableConcept],
        # The status of the marketing authorization.
        "status": FHIR_CodeableConcept,
        # The date at which the given status has become applicable.
        "statusDate": FHIR_dateTime,
        # Extensions for statusDate
        "_statusDate": FHIR_Element,
        # The date when a suspended the marketing or the marketing authorization of the product is anticipated to be restored.
        "restoreDate": FHIR_dateTime,
        # Extensions for restoreDate
        "_restoreDate": FHIR_Element,
        # The beginning of the time period in which the marketing authorization is in the specific status shall be specified A complete date consisting of day, month and year shall be specified using the ISO 8601 date format.
        "validityPeriod": FHIR_Period,
        # A period of time after authorization before generic product applicatiosn can be submitted.
        "dataExclusivityPeriod": FHIR_Period,
        # The date when the first authorization was granted by a Medicines Regulatory Agency.
        "dateOfFirstAuthorization": FHIR_dateTime,
        # Extensions for dateOfFirstAuthorization
        "_dateOfFirstAuthorization": FHIR_Element,
        # Date of first marketing authorization for a company's new medicinal product in any country in the World.
        "internationalBirthDate": FHIR_dateTime,
        # Extensions for internationalBirthDate
        "_internationalBirthDate": FHIR_Element,
        # The legal framework against which this authorization is granted.
        "legalBasis": FHIR_CodeableConcept,
        # Authorization in areas within a country.
        "jurisdictionalAuthorization": List[
            FHIR_MedicinalProductAuthorization_JurisdictionalAuthorization
        ],
        # Marketing Authorization Holder.
        "holder": FHIR_Reference,
        # Medicines Regulatory Agency.
        "regulator": FHIR_Reference,
        # The regulatory procedure for granting or amending a marketing authorization.
        "procedure": FHIR_MedicinalProductAuthorization_Procedure,
    },
    total=False,
)
