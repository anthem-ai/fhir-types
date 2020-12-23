from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_Age import FHIR_Age
from .FHIR_Annotation import FHIR_Annotation
from .FHIR_Attachment import FHIR_Attachment
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_ContactDetail import FHIR_ContactDetail
from .FHIR_ContactPoint import FHIR_ContactPoint
from .FHIR_Contributor import FHIR_Contributor
from .FHIR_Count import FHIR_Count
from .FHIR_DataRequirement import FHIR_DataRequirement
from .FHIR_Distance import FHIR_Distance
from .FHIR_Dosage import FHIR_Dosage
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_Expression import FHIR_Expression
from .FHIR_HumanName import FHIR_HumanName
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Money import FHIR_Money
from .FHIR_ParameterDefinition import FHIR_ParameterDefinition
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Range import FHIR_Range
from .FHIR_Ratio import FHIR_Ratio
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_SampledData import FHIR_SampledData
from .FHIR_Signature import FHIR_Signature
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_TriggerDefinition import FHIR_TriggerDefinition
from .FHIR_UsageContext import FHIR_UsageContext

# This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
FHIR_Parameters_Parameter = TypedDict(
    "FHIR_Parameters_Parameter",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The name of the parameter (reference to the operation definition).
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # If the parameter is a data type.
        "valueBase64Binary": str,
        # Extensions for valueBase64Binary
        "_valueBase64Binary": FHIR_Element,
        # If the parameter is a data type.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # If the parameter is a data type.
        "valueCanonical": str,
        # Extensions for valueCanonical
        "_valueCanonical": FHIR_Element,
        # If the parameter is a data type.
        "valueCode": str,
        # Extensions for valueCode
        "_valueCode": FHIR_Element,
        # If the parameter is a data type.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # If the parameter is a data type.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # If the parameter is a data type.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # If the parameter is a data type.
        "valueId": str,
        # Extensions for valueId
        "_valueId": FHIR_Element,
        # If the parameter is a data type.
        "valueInstant": str,
        # Extensions for valueInstant
        "_valueInstant": FHIR_Element,
        # If the parameter is a data type.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # If the parameter is a data type.
        "valueMarkdown": str,
        # Extensions for valueMarkdown
        "_valueMarkdown": FHIR_Element,
        # If the parameter is a data type.
        "valueOid": str,
        # Extensions for valueOid
        "_valueOid": FHIR_Element,
        # If the parameter is a data type.
        "valuePositiveInt": float,
        # Extensions for valuePositiveInt
        "_valuePositiveInt": FHIR_Element,
        # If the parameter is a data type.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # If the parameter is a data type.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # If the parameter is a data type.
        "valueUnsignedInt": float,
        # Extensions for valueUnsignedInt
        "_valueUnsignedInt": FHIR_Element,
        # If the parameter is a data type.
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # If the parameter is a data type.
        "valueUrl": str,
        # Extensions for valueUrl
        "_valueUrl": FHIR_Element,
        # If the parameter is a data type.
        "valueUuid": str,
        # Extensions for valueUuid
        "_valueUuid": FHIR_Element,
        # If the parameter is a data type.
        "valueAddress": FHIR_Address,
        # If the parameter is a data type.
        "valueAge": FHIR_Age,
        # If the parameter is a data type.
        "valueAnnotation": FHIR_Annotation,
        # If the parameter is a data type.
        "valueAttachment": FHIR_Attachment,
        # If the parameter is a data type.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # If the parameter is a data type.
        "valueCoding": FHIR_Coding,
        # If the parameter is a data type.
        "valueContactPoint": FHIR_ContactPoint,
        # If the parameter is a data type.
        "valueCount": FHIR_Count,
        # If the parameter is a data type.
        "valueDistance": FHIR_Distance,
        # If the parameter is a data type.
        "valueDuration": FHIR_Duration,
        # If the parameter is a data type.
        "valueHumanName": FHIR_HumanName,
        # If the parameter is a data type.
        "valueIdentifier": FHIR_Identifier,
        # If the parameter is a data type.
        "valueMoney": FHIR_Money,
        # If the parameter is a data type.
        "valuePeriod": FHIR_Period,
        # If the parameter is a data type.
        "valueQuantity": FHIR_Quantity,
        # If the parameter is a data type.
        "valueRange": FHIR_Range,
        # If the parameter is a data type.
        "valueRatio": FHIR_Ratio,
        # If the parameter is a data type.
        "valueReference": FHIR_Reference,
        # If the parameter is a data type.
        "valueSampledData": FHIR_SampledData,
        # If the parameter is a data type.
        "valueSignature": FHIR_Signature,
        # If the parameter is a data type.
        "valueTiming": FHIR_Timing,
        # If the parameter is a data type.
        "valueContactDetail": FHIR_ContactDetail,
        # If the parameter is a data type.
        "valueContributor": FHIR_Contributor,
        # If the parameter is a data type.
        "valueDataRequirement": FHIR_DataRequirement,
        # If the parameter is a data type.
        "valueExpression": FHIR_Expression,
        # If the parameter is a data type.
        "valueParameterDefinition": FHIR_ParameterDefinition,
        # If the parameter is a data type.
        "valueRelatedArtifact": FHIR_RelatedArtifact,
        # If the parameter is a data type.
        "valueTriggerDefinition": FHIR_TriggerDefinition,
        # If the parameter is a data type.
        "valueUsageContext": FHIR_UsageContext,
        # If the parameter is a data type.
        "valueDosage": FHIR_Dosage,
        # If the parameter is a data type.
        "valueMeta": FHIR_Meta,
        # If the parameter is a whole resource.
        "resource": Any,
        # A named part of a multi-part parameter.
        "part": List[Any],
    },
    total=False,
)
