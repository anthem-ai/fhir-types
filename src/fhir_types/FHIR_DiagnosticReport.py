from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_DiagnosticReport_Media import FHIR_DiagnosticReport_Media
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_instant import FHIR_instant
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.
FHIR_DiagnosticReport = TypedDict(
    "FHIR_DiagnosticReport",
    {
        # This is a DiagnosticReport resource
        "resourceType": Literal["DiagnosticReport"],
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
        # Identifiers assigned to this report by the performer or other systems.
        "identifier": List[FHIR_Identifier],
        # Details concerning a service requested.
        "basedOn": List[FHIR_Reference],
        # The status of the diagnostic report.
        "status": Literal[
            "registered",
            "partial",
            "preliminary",
            "final",
            "amended",
            "corrected",
            "appended",
            "cancelled",
            "entered-in-error",
            "unknown",
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # A code that classifies the clinical discipline, department or diagnostic service that created the report (e.g. cardiology, biochemistry, hematology, MRI). This is used for searching, sorting and display purposes.
        "category": List[FHIR_CodeableConcept],
        # A code or name that describes this diagnostic report.
        "code": FHIR_CodeableConcept,
        # The subject of the report. Usually, but not always, this is a patient. However, diagnostic services also perform analyses on specimens collected from a variety of other sources.
        "subject": FHIR_Reference,
        # The healthcare event  (e.g. a patient and healthcare provider interaction) which this DiagnosticReport is about.
        "encounter": FHIR_Reference,
        # The time or time-period the observed values are related to. When the subject of the report is a patient, this is usually either the time of the procedure or of specimen collection(s), but very often the source of the date/time is not known, only the date/time itself.
        "effectiveDateTime": str,
        # Extensions for effectiveDateTime
        "_effectiveDateTime": FHIR_Element,
        # The time or time-period the observed values are related to. When the subject of the report is a patient, this is usually either the time of the procedure or of specimen collection(s), but very often the source of the date/time is not known, only the date/time itself.
        "effectivePeriod": FHIR_Period,
        # The date and time that this version of the report was made available to providers, typically after the report was reviewed and verified.
        "issued": FHIR_instant,
        # Extensions for issued
        "_issued": FHIR_Element,
        # The diagnostic service that is responsible for issuing the report.
        "performer": List[FHIR_Reference],
        # The practitioner or organization that is responsible for the report's conclusions and interpretations.
        "resultsInterpreter": List[FHIR_Reference],
        # Details about the specimens on which this diagnostic report is based.
        "specimen": List[FHIR_Reference],
        # [Observations](observation.html)  that are part of this diagnostic report.
        "result": List[FHIR_Reference],
        # One or more links to full details of any imaging performed during the diagnostic investigation. Typically, this is imaging performed by DICOM enabled modalities, but this is not required. A fully enabled PACS viewer can use this information to provide views of the source images.
        "imagingStudy": List[FHIR_Reference],
        # A list of key images associated with this report. The images are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest).
        "media": List[FHIR_DiagnosticReport_Media],
        # Concise and clinically contextualized summary conclusion (interpretation/impression) of the diagnostic report.
        "conclusion": FHIR_string,
        # Extensions for conclusion
        "_conclusion": FHIR_Element,
        # One or more codes that represent the summary conclusion (interpretation/impression) of the diagnostic report.
        "conclusionCode": List[FHIR_CodeableConcept],
        # Rich text representation of the entire result as issued by the diagnostic service. Multiple formats are allowed but they SHALL be semantically equivalent.
        "presentedForm": List[FHIR_Attachment],
    },
    total=False,
)
