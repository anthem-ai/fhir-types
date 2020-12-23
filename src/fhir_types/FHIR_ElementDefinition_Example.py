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

# Captures constraints on each element within the resource, profile, or extension.
FHIR_ElementDefinition_Example = TypedDict(
    "FHIR_ElementDefinition_Example",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Describes the purpose of this example amoung the set of examples.
        "label": FHIR_string,
        # Extensions for label
        "_label": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueBase64Binary": str,
        # Extensions for valueBase64Binary
        "_valueBase64Binary": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueCanonical": str,
        # Extensions for valueCanonical
        "_valueCanonical": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueCode": str,
        # Extensions for valueCode
        "_valueCode": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueId": str,
        # Extensions for valueId
        "_valueId": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueInstant": str,
        # Extensions for valueInstant
        "_valueInstant": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueMarkdown": str,
        # Extensions for valueMarkdown
        "_valueMarkdown": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueOid": str,
        # Extensions for valueOid
        "_valueOid": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valuePositiveInt": float,
        # Extensions for valuePositiveInt
        "_valuePositiveInt": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueUnsignedInt": float,
        # Extensions for valueUnsignedInt
        "_valueUnsignedInt": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueUrl": str,
        # Extensions for valueUrl
        "_valueUrl": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueUuid": str,
        # Extensions for valueUuid
        "_valueUuid": FHIR_Element,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueAddress": FHIR_Address,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueAge": FHIR_Age,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueAnnotation": FHIR_Annotation,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueAttachment": FHIR_Attachment,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueCodeableConcept": FHIR_CodeableConcept,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueCoding": FHIR_Coding,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueContactPoint": FHIR_ContactPoint,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueCount": FHIR_Count,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDistance": FHIR_Distance,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDuration": FHIR_Duration,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueHumanName": FHIR_HumanName,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueIdentifier": FHIR_Identifier,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueMoney": FHIR_Money,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valuePeriod": FHIR_Period,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueQuantity": FHIR_Quantity,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueRange": FHIR_Range,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueRatio": FHIR_Ratio,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueReference": FHIR_Reference,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueSampledData": FHIR_SampledData,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueSignature": FHIR_Signature,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueTiming": FHIR_Timing,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueContactDetail": FHIR_ContactDetail,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueContributor": FHIR_Contributor,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDataRequirement": FHIR_DataRequirement,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueExpression": FHIR_Expression,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueParameterDefinition": FHIR_ParameterDefinition,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueRelatedArtifact": FHIR_RelatedArtifact,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueTriggerDefinition": FHIR_TriggerDefinition,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueUsageContext": FHIR_UsageContext,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueDosage": FHIR_Dosage,
        # The actual value for the element, which must be one of the types allowed for this element.
        "valueMeta": FHIR_Meta,
    },
    total=False,
)
