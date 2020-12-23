from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# The detailed description of a substance, typically at a level beyond what is used for prescribing.
FHIR_SubstanceSpecification_Code = TypedDict(
    "FHIR_SubstanceSpecification_Code",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The specific code.
        "code": FHIR_CodeableConcept,
        # Status of the code assignment.
        "status": FHIR_CodeableConcept,
        # The date at which the code status is changed as part of the terminology maintenance.
        "statusDate": FHIR_dateTime,
        # Extensions for statusDate
        "_statusDate": FHIR_Element,
        # Any comment can be provided in this field, if necessary.
        "comment": FHIR_string,
        # Extensions for comment
        "_comment": FHIR_Element,
        # Supporting literature.
        "source": List[FHIR_Reference],
    },
    total=False,
)
