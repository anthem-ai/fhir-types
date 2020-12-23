from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
FHIR_DetectedIssue_Mitigation = TypedDict(
    "FHIR_DetectedIssue_Mitigation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Describes the action that was taken or the observation that was made that reduces/eliminates the risk associated with the identified issue.
        "action": FHIR_CodeableConcept,
        # Indicates when the mitigating action was documented.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # Identifies the practitioner who determined the mitigation and takes responsibility for the mitigation step occurring.
        "author": FHIR_Reference,
    },
    total=False,
)
