from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Immunization_Education import FHIR_Immunization_Education
from .FHIR_Immunization_Performer import FHIR_Immunization_Performer
from .FHIR_Immunization_ProtocolApplied import FHIR_Immunization_ProtocolApplied
from .FHIR_Immunization_Reaction import FHIR_Immunization_Reaction
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
FHIR_Immunization = TypedDict(
    "FHIR_Immunization",
    {
        # This is a Immunization resource
        "resourceType": Literal["Immunization"],
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
        # A unique identifier assigned to this immunization record.
        "identifier": List[FHIR_Identifier],
        # Indicates the current status of the immunization event.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Indicates the reason the immunization event was not performed.
        "statusReason": FHIR_CodeableConcept,
        # Vaccine that was administered or was to be administered.
        "vaccineCode": FHIR_CodeableConcept,
        # The patient who either received or did not receive the immunization.
        "patient": FHIR_Reference,
        # The visit or admission or other contact between patient and health care provider the immunization was performed as part of.
        "encounter": FHIR_Reference,
        # Date vaccine administered or was to be administered.
        "occurrenceDateTime": str,
        # Extensions for occurrenceDateTime
        "_occurrenceDateTime": FHIR_Element,
        # Date vaccine administered or was to be administered.
        "occurrenceString": str,
        # Extensions for occurrenceString
        "_occurrenceString": FHIR_Element,
        # The date the occurrence of the immunization was first captured in the record - potentially significantly after the occurrence of the event.
        "recorded": FHIR_dateTime,
        # Extensions for recorded
        "_recorded": FHIR_Element,
        # An indication that the content of the record is based on information from the person who administered the vaccine. This reflects the context under which the data was originally recorded.
        "primarySource": FHIR_boolean,
        # Extensions for primarySource
        "_primarySource": FHIR_Element,
        # The source of the data when the report of the immunization event is not based on information from the person who administered the vaccine.
        "reportOrigin": FHIR_CodeableConcept,
        # The service delivery location where the vaccine administration occurred.
        "location": FHIR_Reference,
        # Name of vaccine manufacturer.
        "manufacturer": FHIR_Reference,
        # Lot number of the  vaccine product.
        "lotNumber": FHIR_string,
        # Extensions for lotNumber
        "_lotNumber": FHIR_Element,
        # Date vaccine batch expires.
        "expirationDate": FHIR_date,
        # Extensions for expirationDate
        "_expirationDate": FHIR_Element,
        # Body site where vaccine was administered.
        "site": FHIR_CodeableConcept,
        # The path by which the vaccine product is taken into the body.
        "route": FHIR_CodeableConcept,
        # The quantity of vaccine product that was administered.
        "doseQuantity": FHIR_Quantity,
        # Indicates who performed the immunization event.
        "performer": List[FHIR_Immunization_Performer],
        # Extra information about the immunization that is not conveyed by the other attributes.
        "note": List[FHIR_Annotation],
        # Reasons why the vaccine was administered.
        "reasonCode": List[FHIR_CodeableConcept],
        # Condition, Observation or DiagnosticReport that supports why the immunization was administered.
        "reasonReference": List[FHIR_Reference],
        # Indication if a dose is considered to be subpotent. By default, a dose should be considered to be potent.
        "isSubpotent": FHIR_boolean,
        # Extensions for isSubpotent
        "_isSubpotent": FHIR_Element,
        # Reason why a dose is considered to be subpotent.
        "subpotentReason": List[FHIR_CodeableConcept],
        # Educational material presented to the patient (or guardian) at the time of vaccine administration.
        "education": List[FHIR_Immunization_Education],
        # Indicates a patient's eligibility for a funding program.
        "programEligibility": List[FHIR_CodeableConcept],
        # Indicates the source of the vaccine actually administered. This may be different than the patient eligibility (e.g. the patient may be eligible for a publically purchased vaccine but due to inventory issues, vaccine purchased with private funds was actually administered).
        "fundingSource": FHIR_CodeableConcept,
        # Categorical data indicating that an adverse event is associated in time to an immunization.
        "reaction": List[FHIR_Immunization_Reaction],
        # The protocol (set of recommendations) being followed by the provider who administered the dose.
        "protocolApplied": List[FHIR_Immunization_ProtocolApplied],
    },
    total=False,
)
