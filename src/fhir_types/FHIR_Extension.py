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
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# Optional Extension Element - found in all resources.
FHIR_Extension = TypedDict(
    "FHIR_Extension",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # Source of the definition for the extension code - a logical name or a URL.
        "url": FHIR_uri,
        # Extensions for url
        "_url": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueBase64Binary": str,
        # Extensions for valueBase64Binary
        "_valueBase64Binary": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueBoolean": bool,
        # Extensions for valueBoolean
        "_valueBoolean": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueCanonical": str,
        # Extensions for valueCanonical
        "_valueCanonical": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueCode": str,
        # Extensions for valueCode
        "_valueCode": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDate": str,
        # Extensions for valueDate
        "_valueDate": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDateTime": str,
        # Extensions for valueDateTime
        "_valueDateTime": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDecimal": float,
        # Extensions for valueDecimal
        "_valueDecimal": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueId": str,
        # Extensions for valueId
        "_valueId": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueInstant": str,
        # Extensions for valueInstant
        "_valueInstant": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueInteger": float,
        # Extensions for valueInteger
        "_valueInteger": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueMarkdown": str,
        # Extensions for valueMarkdown
        "_valueMarkdown": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueOid": str,
        # Extensions for valueOid
        "_valueOid": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valuePositiveInt": float,
        # Extensions for valuePositiveInt
        "_valuePositiveInt": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueString": str,
        # Extensions for valueString
        "_valueString": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueTime": str,
        # Extensions for valueTime
        "_valueTime": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueUnsignedInt": float,
        # Extensions for valueUnsignedInt
        "_valueUnsignedInt": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueUri": str,
        # Extensions for valueUri
        "_valueUri": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueUrl": str,
        # Extensions for valueUrl
        "_valueUrl": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueUuid": str,
        # Extensions for valueUuid
        "_valueUuid": FHIR_Element,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueAddress": FHIR_Address,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueAge": FHIR_Age,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueAnnotation": FHIR_Annotation,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueAttachment": FHIR_Attachment,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueCodeableConcept": FHIR_CodeableConcept,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueCoding": FHIR_Coding,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueContactPoint": FHIR_ContactPoint,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueCount": FHIR_Count,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDistance": FHIR_Distance,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDuration": FHIR_Duration,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueHumanName": FHIR_HumanName,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueIdentifier": FHIR_Identifier,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueMoney": FHIR_Money,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valuePeriod": FHIR_Period,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueQuantity": FHIR_Quantity,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueRange": FHIR_Range,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueRatio": FHIR_Ratio,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueReference": FHIR_Reference,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueSampledData": FHIR_SampledData,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueSignature": FHIR_Signature,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueTiming": FHIR_Timing,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueContactDetail": FHIR_ContactDetail,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueContributor": FHIR_Contributor,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDataRequirement": FHIR_DataRequirement,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueExpression": FHIR_Expression,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueParameterDefinition": FHIR_ParameterDefinition,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueRelatedArtifact": FHIR_RelatedArtifact,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueTriggerDefinition": FHIR_TriggerDefinition,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueUsageContext": FHIR_UsageContext,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueDosage": FHIR_Dosage,
        # Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).
        "valueMeta": FHIR_Meta,
    },
    total=False,
)
