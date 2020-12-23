from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_SpecimenDefinition_Container import FHIR_SpecimenDefinition_Container
from .FHIR_SpecimenDefinition_Handling import FHIR_SpecimenDefinition_Handling
from .FHIR_string import FHIR_string

# A kind of specimen with associated set of requirements.
FHIR_SpecimenDefinition_TypeTested = TypedDict(
    "FHIR_SpecimenDefinition_TypeTested",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Primary of secondary specimen.
        "isDerived": FHIR_boolean,
        # Extensions for isDerived
        "_isDerived": FHIR_Element,
        # The kind of specimen conditioned for testing expected by lab.
        "type": FHIR_CodeableConcept,
        # The preference for this type of conditioned specimen.
        "preference": Literal["preferred", "alternate"],
        # Extensions for preference
        "_preference": FHIR_Element,
        # The specimen's container.
        "container": FHIR_SpecimenDefinition_Container,
        # Requirements for delivery and special handling of this kind of conditioned specimen.
        "requirement": FHIR_string,
        # Extensions for requirement
        "_requirement": FHIR_Element,
        # The usual time that a specimen of this kind is retained after the ordered tests are completed, for the purpose of additional testing.
        "retentionTime": FHIR_Duration,
        # Criterion for rejection of the specimen in its container by the laboratory.
        "rejectionCriterion": List[FHIR_CodeableConcept],
        # Set of instructions for preservation/transport of the specimen at a defined temperature interval, prior the testing process.
        "handling": List[FHIR_SpecimenDefinition_Handling],
    },
    total=False,
)
