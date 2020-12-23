from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Raw data describing a biological sequence.
FHIR_MolecularSequence_Repository = TypedDict(
    "FHIR_MolecularSequence_Repository",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Click and see / RESTful API / Need login to see / RESTful API with authentication / Other ways to see resource.
        "type": Literal["directlink", "openapi", "login", "oauth", "other"],
        # Extensions for type
        "_type": FHIR_Element,
        # URI of an external repository which contains further details about the genetics data.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # URI of an external repository which contains further details about the genetics data.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # Id of the variant in this external repository. The server will understand how to use this id to call for more info about datasets in external repository.
        "datasetId": FHIR_string,
        # Extensions for datasetId
        "_datasetId": FHIR_Element,
        # Id of the variantset in this external repository. The server will understand how to use this id to call for more info about variantsets in external repository.
        "variantsetId": FHIR_string,
        # Extensions for variantsetId
        "_variantsetId": FHIR_Element,
        # Id of the read in this external repository.
        "readsetId": FHIR_string,
        # Extensions for readsetId
        "_readsetId": FHIR_Element,
    },
    total=False,
)
