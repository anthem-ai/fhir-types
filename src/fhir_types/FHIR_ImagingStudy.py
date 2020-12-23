from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_ImagingStudy_Series import FHIR_ImagingStudy_Series
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_uri import FHIR_uri

# Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
FHIR_ImagingStudy = TypedDict(
    "FHIR_ImagingStudy",
    {
        # This is a ImagingStudy resource
        "resourceType": Literal["ImagingStudy"],
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
        # Identifiers for the ImagingStudy such as DICOM Study Instance UID, and Accession Number.
        "identifier": List[FHIR_Identifier],
        # The current state of the ImagingStudy.
        "status": Literal[
            "registered", "available", "cancelled", "entered-in-error", "unknown"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # A list of all the series.modality values that are actual acquisition modalities, i.e. those in the DICOM Context Group 29 (value set OID 1.2.840.10008.6.1.19).
        "modality": List[FHIR_Coding],
        # The subject, typically a patient, of the imaging study.
        "subject": FHIR_Reference,
        # The healthcare event (e.g. a patient and healthcare provider interaction) during which this ImagingStudy is made.
        "encounter": FHIR_Reference,
        # Date and time the study started.
        "started": FHIR_dateTime,
        # Extensions for started
        "_started": FHIR_Element,
        # A list of the diagnostic requests that resulted in this imaging study being performed.
        "basedOn": List[FHIR_Reference],
        # The requesting/referring physician.
        "referrer": FHIR_Reference,
        # Who read the study and interpreted the images or other content.
        "interpreter": List[FHIR_Reference],
        # The network service providing access (e.g., query, view, or retrieval) for the study. See implementation notes for information about using DICOM endpoints. A study-level endpoint applies to each series in the study, unless overridden by a series-level endpoint with the same Endpoint.connectionType.
        "endpoint": List[FHIR_Reference],
        # Number of Series in the Study. This value given may be larger than the number of series elements this Resource contains due to resource availability, security, or other factors. This element should be present if any series elements are present.
        "numberOfSeries": FHIR_unsignedInt,
        # Extensions for numberOfSeries
        "_numberOfSeries": FHIR_Element,
        # Number of SOP Instances in Study. This value given may be larger than the number of instance elements this resource contains due to resource availability, security, or other factors. This element should be present if any instance elements are present.
        "numberOfInstances": FHIR_unsignedInt,
        # Extensions for numberOfInstances
        "_numberOfInstances": FHIR_Element,
        # The procedure which this ImagingStudy was part of.
        "procedureReference": FHIR_Reference,
        # The code for the performed procedure type.
        "procedureCode": List[FHIR_CodeableConcept],
        # The principal physical location where the ImagingStudy was performed.
        "location": FHIR_Reference,
        # Description of clinical condition indicating why the ImagingStudy was requested.
        "reasonCode": List[FHIR_CodeableConcept],
        # Indicates another resource whose existence justifies this Study.
        "reasonReference": List[FHIR_Reference],
        # Per the recommended DICOM mapping, this element is derived from the Study Description attribute (0008,1030). Observations or findings about the imaging study should be recorded in another resource, e.g. Observation, and not in this element.
        "note": List[FHIR_Annotation],
        # The Imaging Manager description of the study. Institution-generated description or classification of the Study (component) performed.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Each study has one or more series of images or other content.
        "series": List[FHIR_ImagingStudy_Series],
    },
    total=False,
)
