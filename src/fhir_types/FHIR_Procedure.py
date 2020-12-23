from typing import Any, List, Literal, TypedDict

from .FHIR_Age import FHIR_Age
from .FHIR_Annotation import FHIR_Annotation
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Procedure_FocalDevice import FHIR_Procedure_FocalDevice
from .FHIR_Procedure_Performer import FHIR_Procedure_Performer
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.
FHIR_Procedure = TypedDict(
    "FHIR_Procedure",
    {
        # This is a Procedure resource
        "resourceType": Literal["Procedure"],
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
        # Business identifiers assigned to this procedure by the performer or other systems which remain constant as the resource is updated and is propagated from server to server.
        "identifier": List[FHIR_Identifier],
        # The URL pointing to a FHIR-defined protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.
        "instantiatesCanonical": List[FHIR_canonical],
        # The URL pointing to an externally maintained protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.
        "instantiatesUri": List[FHIR_uri],
        # Extensions for instantiatesUri
        "_instantiatesUri": List[FHIR_Element],
        # A reference to a resource that contains details of the request for this procedure.
        "basedOn": List[FHIR_Reference],
        # A larger event of which this particular procedure is a component or step.
        "partOf": List[FHIR_Reference],
        # A code specifying the state of the procedure. Generally, this will be the in-progress or completed state.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # Captures the reason for the current state of the procedure.
        "statusReason": FHIR_CodeableConcept,
        # A code that classifies the procedure for searching, sorting and display purposes (e.g. "Surgical Procedure").
        "category": FHIR_CodeableConcept,
        # The specific procedure that is performed. Use text if the exact nature of the procedure cannot be coded (e.g. "Laparoscopic Appendectomy").
        "code": FHIR_CodeableConcept,
        # The person, animal or group on which the procedure was performed.
        "subject": FHIR_Reference,
        # The Encounter during which this Procedure was created or performed or to which the creation of this record is tightly associated.
        "encounter": FHIR_Reference,
        # Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.
        "performedDateTime": str,
        # Extensions for performedDateTime
        "_performedDateTime": FHIR_Element,
        # Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.
        "performedPeriod": FHIR_Period,
        # Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.
        "performedString": str,
        # Extensions for performedString
        "_performedString": FHIR_Element,
        # Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.
        "performedAge": FHIR_Age,
        # Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.
        "performedRange": FHIR_Range,
        # Individual who recorded the record and takes responsibility for its content.
        "recorder": FHIR_Reference,
        # Individual who is making the procedure statement.
        "asserter": FHIR_Reference,
        # Limited to "real" people rather than equipment.
        "performer": List[FHIR_Procedure_Performer],
        # The location where the procedure actually happened.  E.g. a newborn at home, a tracheostomy at a restaurant.
        "location": FHIR_Reference,
        # The coded reason why the procedure was performed. This may be a coded entity of some type, or may simply be present as text.
        "reasonCode": List[FHIR_CodeableConcept],
        # The justification of why the procedure was performed.
        "reasonReference": List[FHIR_Reference],
        # Detailed and structured anatomical location information. Multiple locations are allowed - e.g. multiple punch biopsies of a lesion.
        "bodySite": List[FHIR_CodeableConcept],
        # The outcome of the procedure - did it resolve the reasons for the procedure being performed?
        "outcome": FHIR_CodeableConcept,
        # This could be a histology result, pathology report, surgical report, etc.
        "report": List[FHIR_Reference],
        # Any complications that occurred during the procedure, or in the immediate post-performance period. These are generally tracked separately from the notes, which will typically describe the procedure itself rather than any 'post procedure' issues.
        "complication": List[FHIR_CodeableConcept],
        # Any complications that occurred during the procedure, or in the immediate post-performance period.
        "complicationDetail": List[FHIR_Reference],
        # If the procedure required specific follow up - e.g. removal of sutures. The follow up may be represented as a simple note or could potentially be more complex, in which case the CarePlan resource can be used.
        "followUp": List[FHIR_CodeableConcept],
        # Any other notes and comments about the procedure.
        "note": List[FHIR_Annotation],
        # A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.
        "focalDevice": List[FHIR_Procedure_FocalDevice],
        # Identifies medications, devices and any other substance used as part of the procedure.
        "usedReference": List[FHIR_Reference],
        # Identifies coded items that were used as part of the procedure.
        "usedCode": List[FHIR_CodeableConcept],
    },
    total=False,
)
