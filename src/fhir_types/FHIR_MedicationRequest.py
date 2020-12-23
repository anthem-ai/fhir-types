from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_boolean import FHIR_boolean
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Dosage import FHIR_Dosage
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_MedicationRequest_DispenseRequest import (
    FHIR_MedicationRequest_DispenseRequest,
)
from .FHIR_MedicationRequest_Substitution import FHIR_MedicationRequest_Substitution
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
FHIR_MedicationRequest = TypedDict(
    "FHIR_MedicationRequest",
    {
        # This is a MedicationRequest resource
        "resourceType": Literal["MedicationRequest"],
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
        # Identifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to server.
        "identifier": List[FHIR_Identifier],
        # A code specifying the current state of the order.  Generally, this will be active or completed state.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Captures the reason for the current state of the MedicationRequest.
        "statusReason": FHIR_CodeableConcept,
        # Whether the request is a proposal, plan, or an original order.
        "intent": FHIR_code,
        # Extensions for intent
        "_intent": FHIR_Element,
        # Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient)).
        "category": List[FHIR_CodeableConcept],
        # Indicates how quickly the Medication Request should be addressed with respect to other requests.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # If true indicates that the provider is asking for the medication request not to occur.
        "doNotPerform": FHIR_boolean,
        # Extensions for doNotPerform
        "_doNotPerform": FHIR_Element,
        # Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record.  It may also indicate the source of the report.
        "reportedBoolean": bool,
        # Extensions for reportedBoolean
        "_reportedBoolean": FHIR_Element,
        # Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record.  It may also indicate the source of the report.
        "reportedReference": FHIR_Reference,
        # Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medications.
        "medicationCodeableConcept": FHIR_CodeableConcept,
        # Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medications.
        "medicationReference": FHIR_Reference,
        # A link to a resource representing the person or set of individuals to whom the medication will be given.
        "subject": FHIR_Reference,
        # The Encounter during which this [x] was created or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # Include additional information (for example, patient height and weight) that supports the ordering of the medication.
        "supportingInformation": List[FHIR_Reference],
        # The date (and perhaps time) when the prescription was initially written or authored on.
        "authoredOn": FHIR_dateTime,
        # Extensions for authoredOn
        "_authoredOn": FHIR_Element,
        # The individual, organization, or device that initiated the request and has responsibility for its activation.
        "requester": FHIR_Reference,
        # The specified desired performer of the medication treatment (e.g. the performer of the medication administration).
        "performer": FHIR_Reference,
        # Indicates the type of performer of the administration of the medication.
        "performerType": FHIR_CodeableConcept,
        # The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone order.
        "recorder": FHIR_Reference,
        # The reason or the indication for ordering or not ordering the medication.
        "reasonCode": List[FHIR_CodeableConcept],
        # Condition or observation that supports why the medication was ordered.
        "reasonReference": List[FHIR_Reference],
        # The URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequest.
        "instantiatesCanonical": List[FHIR_canonical],
        # Extensions for instantiatesCanonical
        "_instantiatesCanonical": List[FHIR_Element],
        # The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequest.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # A plan or request that is fulfilled in whole or in part by this medication request.
        "basedOn": List[FHIR_Reference],
        # A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescription.
        "groupIdentifier": FHIR_Identifier,
        # The description of the overall patte3rn of the administration of the medication to the patient.
        "courseOfTherapyType": FHIR_CodeableConcept,
        # Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested service.
        "insurance": List[FHIR_Reference],
        # Extra information about the prescription that could not be conveyed by the other attributes.
        "note": List[FHIR_Annotation],
        # Indicates how the medication is to be used by the patient.
        "dosageInstruction": List[FHIR_Dosage],
        # Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy department.
        "dispenseRequest": FHIR_MedicationRequest_DispenseRequest,
        # Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done.
        "substitution": FHIR_MedicationRequest_Substitution,
        # A link to a resource representing an earlier order related order or prescription.
        "priorPrescription": FHIR_Reference,
        # Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etc.
        "detectedIssue": List[FHIR_Reference],
        # Links to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resource.
        "eventHistory": List[FHIR_Reference],
    },
    total=False,
)
