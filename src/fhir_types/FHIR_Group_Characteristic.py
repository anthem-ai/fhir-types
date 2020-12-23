from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
FHIR_Group_Characteristic = TypedDict(
    "FHIR_Group_Characteristic",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A code that identifies the kind of trait being asserted.
        "code": FHIR_CodeableConcept,
        # The value of the trait that holds (or does not hold - see 'exclude') for members of the group.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # The value of the trait that holds (or does not hold - see 'exclude') for members of the group.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The value of the trait that holds (or does not hold - see 'exclude') for members of the group.
        "valueQuantity": FHIR_Quantity,
        # The value of the trait that holds (or does not hold - see 'exclude') for members of the group.
        "valueRange": FHIR_Range,
        # The value of the trait that holds (or does not hold - see 'exclude') for members of the group.
        "valueReference": FHIR_Reference,
        # If true, indicates the characteristic is one that is NOT held by members of the group.
        "exclude": FHIR_boolean,
        # Extensions for exclude
        "_exclude": FHIR_Element,
        # The period over which the characteristic is tested; e.g. the patient had an operation during the month of June.
        "period": FHIR_Period,
    },
    total=False,
)
