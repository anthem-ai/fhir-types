from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Consent_Policy import FHIR_Consent_Policy
from .FHIR_Consent_Provision import FHIR_Consent_Provision
from .FHIR_Consent_Verification import FHIR_Consent_Verification
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
FHIR_Consent = TypedDict(
    "FHIR_Consent",
    {
        # This is a Consent resource
        "resourceType": Literal["Consent"],
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
        # Unique identifier for this copy of the Consent Statement.
        "identifier": List[FHIR_Identifier],
        # Indicates the current state of this consent.
        "status": Literal[
            "draft", "proposed", "active", "rejected", "inactive", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible.
        "scope": FHIR_CodeableConcept,
        # A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.
        "category": List[FHIR_CodeableConcept],
        # The patient/healthcare consumer to whom this consent applies.
        "patient": FHIR_Reference,
        # When this  Consent was issued / created / indexed.
        "dateTime": FHIR_dateTime,
        # Extensions for dateTime
        "_dateTime": FHIR_Element,
        # Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.
        "performer": List[FHIR_Reference],
        # The organization that manages the consent, and the framework within which it is executed.
        "organization": List[FHIR_Reference],
        # The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository (e.g. XDS) that stores the original consent document.
        "sourceAttachment": FHIR_Attachment,
        # The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository (e.g. XDS) that stores the original consent document.
        "sourceReference": FHIR_Reference,
        # The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.
        "policy": List[FHIR_Consent_Policy],
        # A reference to the specific base computable regulation or policy.
        "policyRule": FHIR_CodeableConcept,
        # Whether a treatment instruction (e.g. artificial respiration yes or no) was verified with the patient, his/her family or another authorized person.
        "verification": List[FHIR_Consent_Verification],
        # An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.
        "provision": FHIR_Consent_Provision,
    },
    total=False,
)
