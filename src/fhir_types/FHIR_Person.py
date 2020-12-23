from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_Attachment import FHIR_Attachment
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_date import FHIR_date
from .FHIR_Element import FHIR_Element
from .FHIR_HumanName import FHIR_HumanName
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Person_Link import FHIR_Person_Link
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# Demographics and administrative information about a person independent of a specific health-related context.
FHIR_Person = TypedDict(
    "FHIR_Person",
    {
        # This is a Person resource
        "resourceType": Literal["Person"],
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
        # Identifier for a person within a particular scope.
        "identifier": List[FHIR_Identifier],
        # A name associated with the person.
        "name": List[FHIR_HumanName],
        # A contact detail for the person, e.g. a telephone number or an email address.
        "telecom": List[FHIR_ContactPoint],
        # Administrative Gender.
        "gender": Literal["male", "female", "other", "unknown"],
        # Extensions for gender
        "_gender": FHIR_Element,
        # The birth date for the person.
        "birthDate": FHIR_date,
        # Extensions for birthDate
        "_birthDate": FHIR_Element,
        # One or more addresses for the person.
        "address": List[FHIR_Address],
        # An image that can be displayed as a thumbnail of the person to enhance the identification of the individual.
        "photo": FHIR_Attachment,
        # The organization that is the custodian of the person record.
        "managingOrganization": FHIR_Reference,
        # Whether this person's record is in active use.
        "active": FHIR_boolean,
        # Extensions for active
        "_active": FHIR_Element,
        # Link to a resource that concerns the same actual person.
        "link": List[FHIR_Person_Link],
    },
    total=False,
)
