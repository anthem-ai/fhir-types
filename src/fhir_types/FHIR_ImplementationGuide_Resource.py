from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string

# A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
FHIR_ImplementationGuide_Resource = TypedDict(
    "FHIR_ImplementationGuide_Resource",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Where this resource is found.
        "reference": FHIR_Reference,
        # Indicates the FHIR Version(s) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.
        "fhirVersion": List[
            Literal[
                "0.01",
                "0.05",
                "0.06",
                "0.11",
                "0.0.80",
                "0.0.81",
                "0.0.82",
                "0.4.0",
                "0.5.0",
                "1.0.0",
                "1.0.1",
                "1.0.2",
                "1.1.0",
                "1.4.0",
                "1.6.0",
                "1.8.0",
                "3.0.0",
                "3.0.1",
                "3.3.0",
                "3.5.0",
                "4.0.0",
                "4.0.1",
            ]
        ],
        # Extensions for fhirVersion
        "_fhirVersion": List[FHIR_Element],
        # A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource (e.g. ValueSet.name).
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # A description of the reason that a resource has been included in the implementation guide.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.
        "exampleBoolean": bool,
        # Extensions for exampleBoolean
        "_exampleBoolean": FHIR_Element,
        # If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.
        "exampleCanonical": str,
        # Extensions for exampleCanonical
        "_exampleCanonical": FHIR_Element,
        # Reference to the id of the grouping this resource appears in.
        "groupingId": FHIR_id,
        # Extensions for groupingId
        "_groupingId": FHIR_Element,
    },
    total=False,
)
