from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_uri import FHIR_uri
from .FHIR_VerificationResult_Attestation import FHIR_VerificationResult_Attestation
from .FHIR_VerificationResult_PrimarySource import FHIR_VerificationResult_PrimarySource
from .FHIR_VerificationResult_Validator import FHIR_VerificationResult_Validator

# Describes validation requirements, source(s), status and dates for one or more elements.
FHIR_VerificationResult = TypedDict(
    "FHIR_VerificationResult",
    {
        # This is a VerificationResult resource
        "resourceType": Literal["VerificationResult"],
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
        # A resource that was validated.
        "target": List[FHIR_Reference],
        # The fhirpath location(s) within the resource that was validated.
        "targetLocation": List[FHIR_string],
        # Extensions for targetLocation
        "_targetLocation": List[FHIR_Element],
        # The frequency with which the target must be validated (none; initial; periodic).
        "need": FHIR_CodeableConcept,
        # The validation status of the target (attested; validated; in process; requires revalidation; validation failed; revalidation failed).
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # When the validation status was updated.
        "statusDate": FHIR_dateTime,
        # Extensions for statusDate
        "_statusDate": FHIR_Element,
        # What the target is validated against (nothing; primary source; multiple sources).
        "validationType": FHIR_CodeableConcept,
        # The primary process by which the target is validated (edit check; value set; primary source; multiple sources; standalone; in context).
        "validationProcess": List[FHIR_CodeableConcept],
        # Frequency of revalidation.
        "frequency": FHIR_Timing,
        # The date/time validation was last completed (including failed validations).
        "lastPerformed": FHIR_dateTime,
        # Extensions for lastPerformed
        "_lastPerformed": FHIR_Element,
        # The date when target is next validated, if appropriate.
        "nextScheduled": FHIR_date,
        # Extensions for nextScheduled
        "_nextScheduled": FHIR_Element,
        # The result if validation fails (fatal; warning; record only; none).
        "failureAction": FHIR_CodeableConcept,
        # Information about the primary source(s) involved in validation.
        "primarySource": List[FHIR_VerificationResult_PrimarySource],
        # Information about the entity attesting to information.
        "attestation": FHIR_VerificationResult_Attestation,
        # Information about the entity validating information.
        "validator": List[FHIR_VerificationResult_Validator],
    },
    total=False,
)
