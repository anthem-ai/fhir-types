from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
FHIR_ImmunizationEvaluation = TypedDict(
    "FHIR_ImmunizationEvaluation",
    {
        # This is a ImmunizationEvaluation resource
        "resourceType": Literal["ImmunizationEvaluation"],
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
        # A unique identifier assigned to this immunization evaluation record.
        "identifier": List[FHIR_Identifier],
        # Indicates the current status of the evaluation of the vaccination administration event.
        "status": FHIR_code,
        # Extensions for status
        "_status": FHIR_Element,
        # The individual for whom the evaluation is being done.
        "patient": FHIR_Reference,
        # The date the evaluation of the vaccine administration event was performed.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Indicates the authority who published the protocol (e.g. ACIP).
        "authority": FHIR_Reference,
        # The vaccine preventable disease the dose is being evaluated against.
        "targetDisease": FHIR_CodeableConcept,
        # The vaccine administration event being evaluated.
        "immunizationEvent": FHIR_Reference,
        # Indicates if the dose is valid or not valid with respect to the published recommendations.
        "doseStatus": FHIR_CodeableConcept,
        # Provides an explanation as to why the vaccine administration event is valid or not relative to the published recommendations.
        "doseStatusReason": List[FHIR_CodeableConcept],
        # Additional information about the evaluation.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # One possible path to achieve presumed immunity against a disease - within the context of an authority.
        "series": FHIR_string,
        # Extensions for series
        "_series": FHIR_Element,
        # Nominal position in a series.
        "doseNumberPositiveInt": float,
        # Extensions for doseNumberPositiveInt
        "_doseNumberPositiveInt": FHIR_Element,
        # Nominal position in a series.
        "doseNumberString": str,
        # Extensions for doseNumberString
        "_doseNumberString": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesPositiveInt": float,
        # Extensions for seriesDosesPositiveInt
        "_seriesDosesPositiveInt": FHIR_Element,
        # The recommended number of doses to achieve immunity.
        "seriesDosesString": str,
        # Extensions for seriesDosesString
        "_seriesDosesString": FHIR_Element,
    },
    total=False,
)
