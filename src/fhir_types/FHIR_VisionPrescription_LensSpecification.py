from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_integer import FHIR_integer
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_string import FHIR_string
from .FHIR_VisionPrescription_Prism import FHIR_VisionPrescription_Prism

# An authorization for the provision of glasses and/or contact lenses to a patient.
FHIR_VisionPrescription_LensSpecification = TypedDict(
    "FHIR_VisionPrescription_LensSpecification",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifies the type of vision correction product which is required for the patient.
        "product": FHIR_CodeableConcept,
        # The eye for which the lens specification applies.
        "eye": Literal["right", "left"],
        # Extensions for eye
        "_eye": FHIR_Element,
        # Lens power measured in dioptres (0.25 units).
        "sphere": FHIR_decimal,
        # Extensions for sphere
        "_sphere": FHIR_Element,
        # Power adjustment for astigmatism measured in dioptres (0.25 units).
        "cylinder": FHIR_decimal,
        # Extensions for cylinder
        "_cylinder": FHIR_Element,
        # Adjustment for astigmatism measured in integer degrees.
        "axis": FHIR_integer,
        # Extensions for axis
        "_axis": FHIR_Element,
        # Allows for adjustment on two axis.
        "prism": List[FHIR_VisionPrescription_Prism],
        # Power adjustment for multifocal lenses measured in dioptres (0.25 units).
        "add": FHIR_decimal,
        # Extensions for add
        "_add": FHIR_Element,
        # Contact lens power measured in dioptres (0.25 units).
        "power": FHIR_decimal,
        # Extensions for power
        "_power": FHIR_Element,
        # Back curvature measured in millimetres.
        "backCurve": FHIR_decimal,
        # Extensions for backCurve
        "_backCurve": FHIR_Element,
        # Contact lens diameter measured in millimetres.
        "diameter": FHIR_decimal,
        # Extensions for diameter
        "_diameter": FHIR_Element,
        # The recommended maximum wear period for the lens.
        "duration": FHIR_Quantity,
        # Special color or pattern.
        "color": FHIR_string,
        # Extensions for color
        "_color": FHIR_Element,
        # Brand recommendations or restrictions.
        "brand": FHIR_string,
        # Extensions for brand
        "_brand": FHIR_Element,
        # Notes for special requirements such as coatings and lens materials.
        "note": List[FHIR_Annotation],
    },
    total=False,
)
