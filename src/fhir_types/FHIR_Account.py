from typing import Any, List, Literal, TypedDict

from .FHIR_Account_Coverage import FHIR_Account_Coverage
from .FHIR_Account_Guarantor import FHIR_Account_Guarantor
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
FHIR_Account = TypedDict(
    "FHIR_Account",
    {
        # This is a Account resource
        "resourceType": Literal["Account"],
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
        # Unique identifier used to reference the account.  Might or might not be intended for human use (e.g. credit card number).
        "identifier": List[FHIR_Identifier],
        # Indicates whether the account is presently used/usable or not.
        "status": Literal[
            "active", "inactive", "entered-in-error", "on-hold", "unknown"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # Categorizes the account for reporting and searching purposes.
        "type": FHIR_CodeableConcept,
        # Name used for the account when displaying it to humans in reports, etc.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Identifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the Account.
        "subject": List[FHIR_Reference],
        # The date range of services associated with this account.
        "servicePeriod": FHIR_Period,
        # The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account.
        "coverage": List[FHIR_Account_Coverage],
        # Indicates the service area, hospital, department, etc. with responsibility for managing the Account.
        "owner": FHIR_Reference,
        # Provides additional information about what the account tracks and how it is used.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # The parties responsible for balancing the account if other payment options fall short.
        "guarantor": List[FHIR_Account_Guarantor],
        # Reference to a parent Account.
        "partOf": FHIR_Reference,
    },
    total=False,
)
