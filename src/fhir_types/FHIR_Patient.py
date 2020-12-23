from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_Attachment import FHIR_Attachment
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_date import FHIR_date
from .FHIR_Element import FHIR_Element
from .FHIR_HumanName import FHIR_HumanName
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Patient_Communication import FHIR_Patient_Communication
from .FHIR_Patient_Contact import FHIR_Patient_Contact
from .FHIR_Patient_Link import FHIR_Patient_Link
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# Demographics and other administrative information about an individual or animal receiving care or other health-related services.
FHIR_Patient = TypedDict(
    "FHIR_Patient",
    {
        # This is a Patient resource
        "resourceType": Literal["Patient"],
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
        # An identifier for this patient.
        "identifier": List[FHIR_Identifier],
        # Whether this patient record is in active use. Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules.It is often used to filter patient lists to exclude inactive patientsDeceased patients may also be marked as inactive for the same reasons, but may be active for some time after death.
        "active": FHIR_boolean,
        # Extensions for active
        "_active": FHIR_Element,
        # A name associated with the individual.
        "name": List[FHIR_HumanName],
        # A contact detail (e.g. a telephone number or an email address) by which the individual may be contacted.
        "telecom": List[FHIR_ContactPoint],
        # Administrative Gender - the gender that the patient is considered to have for administration and record keeping purposes.
        "gender": Literal["male", "female", "other", "unknown"],
        # Extensions for gender
        "_gender": FHIR_Element,
        # The date of birth for the individual.
        "birthDate": FHIR_date,
        # Extensions for birthDate
        "_birthDate": FHIR_Element,
        # Indicates if the individual is deceased or not.
        "deceasedBoolean": bool,
        # Extensions for deceasedBoolean
        "_deceasedBoolean": FHIR_Element,
        # Indicates if the individual is deceased or not.
        "deceasedDateTime": str,
        # Extensions for deceasedDateTime
        "_deceasedDateTime": FHIR_Element,
        # An address for the individual.
        "address": List[FHIR_Address],
        # This field contains a patient's most recent marital (civil) status.
        "maritalStatus": FHIR_CodeableConcept,
        # Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer).
        "multipleBirthBoolean": bool,
        # Extensions for multipleBirthBoolean
        "_multipleBirthBoolean": FHIR_Element,
        # Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer).
        "multipleBirthInteger": float,
        # Extensions for multipleBirthInteger
        "_multipleBirthInteger": FHIR_Element,
        # Image of the patient.
        "photo": List[FHIR_Attachment],
        # A contact party (e.g. guardian, partner, friend) for the patient.
        "contact": List[FHIR_Patient_Contact],
        # A language which may be used to communicate with the patient about his or her health.
        "communication": List[FHIR_Patient_Communication],
        # Patient's nominated care provider.
        "generalPractitioner": List[FHIR_Reference],
        # Organization that is the custodian of the patient record.
        "managingOrganization": FHIR_Reference,
        # Link to another patient resource that concerns the same actual patient.
        "link": List[FHIR_Patient_Link],
    },
    total=False,
)
