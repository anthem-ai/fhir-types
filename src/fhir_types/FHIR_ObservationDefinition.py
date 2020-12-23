from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_ObservationDefinition_QualifiedInterval import (
    FHIR_ObservationDefinition_QualifiedInterval,
)
from .FHIR_ObservationDefinition_QuantitativeDetails import (
    FHIR_ObservationDefinition_QuantitativeDetails,
)
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
FHIR_ObservationDefinition = TypedDict(
    "FHIR_ObservationDefinition",
    {
        # This is a ObservationDefinition resource
        "resourceType": Literal["ObservationDefinition"],
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
        # A code that classifies the general type of observation.
        "category": List[FHIR_CodeableConcept],
        # Describes what will be observed. Sometimes this is called the observation "name".
        "code": FHIR_CodeableConcept,
        # A unique identifier assigned to this ObservationDefinition artifact.
        "identifier": List[FHIR_Identifier],
        # The data types allowed for the value element of the instance observations conforming to this ObservationDefinition.
        "permittedDataType": List[
            Literal[
                "Quantity",
                "CodeableConcept",
                "string",
                "boolean",
                "integer",
                "Range",
                "Ratio",
                "SampledData",
                "time",
                "dateTime",
                "Period",
            ]
        ],
        # Extensions for permittedDataType
        "_permittedDataType": List[FHIR_Element],
        # Multiple results allowed for observations conforming to this ObservationDefinition.
        "multipleResultsAllowed": FHIR_boolean,
        # Extensions for multipleResultsAllowed
        "_multipleResultsAllowed": FHIR_Element,
        # The method or technique used to perform the observation.
        "method": FHIR_CodeableConcept,
        # The preferred name to be used when reporting the results of observations conforming to this ObservationDefinition.
        "preferredReportName": FHIR_string,
        # Extensions for preferredReportName
        "_preferredReportName": FHIR_Element,
        # Characteristics for quantitative results of this observation.
        "quantitativeDetails": FHIR_ObservationDefinition_QuantitativeDetails,
        # Multiple  ranges of results qualified by different contexts for ordinal or continuous observations conforming to this ObservationDefinition.
        "qualifiedInterval": List[FHIR_ObservationDefinition_QualifiedInterval],
        # The set of valid coded results for the observations  conforming to this ObservationDefinition.
        "validCodedValueSet": FHIR_Reference,
        # The set of normal coded results for the observations conforming to this ObservationDefinition.
        "normalCodedValueSet": FHIR_Reference,
        # The set of abnormal coded results for the observation conforming to this ObservationDefinition.
        "abnormalCodedValueSet": FHIR_Reference,
        # The set of critical coded results for the observation conforming to this ObservationDefinition.
        "criticalCodedValueSet": FHIR_Reference,
    },
    total=False,
)
