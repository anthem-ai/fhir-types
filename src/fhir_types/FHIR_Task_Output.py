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

# A task to be performed.
FHIR_Task_Output = TypedDict(
    "FHIR_Task_Output",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The name of the Output parameter.
        "type": FHIR_CodeableConcept,
        # The value of the Output parameter as a basic type.
        "valueBase64Binary": str,
        # Extensions for valueBase64Binary
        "_valueBase64Binary": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueCanonical": str,
        # Extensions for valueCanonical
        "_valueCanonical": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueCode": str,
        # Extensions for valueCode
        "_valueCode": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueId": str,
        # Extensions for valueId
        "_valueId": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueInstant": str,
        # Extensions for valueInstant
        "_valueInstant": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueMarkdown": str,
        # Extensions for valueMarkdown
        "_valueMarkdown": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueOid": str,
        # Extensions for valueOid
        "_valueOid": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valuePositiveInt": float,
        # Extensions for valuePositiveInt
        "_valuePositiveInt": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueUnsignedInt": float,
        # Extensions for valueUnsignedInt
        "_valueUnsignedInt": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueUrl": str,
        # Extensions for valueUrl
        "_valueUrl": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueUuid": str,
        # Extensions for valueUuid
        "_valueUuid": FHIR_Element,
        # The value of the Output parameter as a basic type.
        "valueAddress": FHIR_Address,
        # The value of the Output parameter as a basic type.
        "valueAge": FHIR_Age,
        # The value of the Output parameter as a basic type.
        "valueAnnotation": FHIR_Annotation,
        # The value of the Output parameter as a basic type.
        "valueAttachment": FHIR_Attachment,
        # The value of the Output parameter as a basic type.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # The value of the Output parameter as a basic type.
        "valueCoding": FHIR_Coding,
        # The value of the Output parameter as a basic type.
        "valueContactPoint": FHIR_ContactPoint,
        # The value of the Output parameter as a basic type.
        "valueCount": FHIR_Count,
        # The value of the Output parameter as a basic type.
        "valueDistance": FHIR_Distance,
        # The value of the Output parameter as a basic type.
        "valueDuration": FHIR_Duration,
        # The value of the Output parameter as a basic type.
        "valueHumanName": FHIR_HumanName,
        # The value of the Output parameter as a basic type.
        "valueIdentifier": FHIR_Identifier,
        # The value of the Output parameter as a basic type.
        "valueMoney": FHIR_Money,
        # The value of the Output parameter as a basic type.
        "valuePeriod": FHIR_Period,
        # The value of the Output parameter as a basic type.
        "valueQuantity": FHIR_Quantity,
        # The value of the Output parameter as a basic type.
        "valueRange": FHIR_Range,
        # The value of the Output parameter as a basic type.
        "valueRatio": FHIR_Ratio,
        # The value of the Output parameter as a basic type.
        "valueReference": FHIR_Reference,
        # The value of the Output parameter as a basic type.
        "valueSampledData": FHIR_SampledData,
        # The value of the Output parameter as a basic type.
        "valueSignature": FHIR_Signature,
        # The value of the Output parameter as a basic type.
        "valueTiming": FHIR_Timing,
        # The value of the Output parameter as a basic type.
        "valueContactDetail": FHIR_ContactDetail,
        # The value of the Output parameter as a basic type.
        "valueContributor": FHIR_Contributor,
        # The value of the Output parameter as a basic type.
        "valueDataRequirement": FHIR_DataRequirement,
        # The value of the Output parameter as a basic type.
        "valueExpression": FHIR_Expression,
        # The value of the Output parameter as a basic type.
        "valueParameterDefinition": FHIR_ParameterDefinition,
        # The value of the Output parameter as a basic type.
        "valueRelatedArtifact": FHIR_RelatedArtifact,
        # The value of the Output parameter as a basic type.
        "valueTriggerDefinition": FHIR_TriggerDefinition,
        # The value of the Output parameter as a basic type.
        "valueUsageContext": FHIR_UsageContext,
        # The value of the Output parameter as a basic type.
        "valueDosage": FHIR_Dosage,
        # The value of the Output parameter as a basic type.
        "valueMeta": FHIR_Meta,
    },
    total=False,
)
