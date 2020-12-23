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
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_integer import FHIR_integer
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

# A Map of relationships between 2 structures that can be used to transform data.
FHIR_StructureMap_Source = TypedDict(
    "FHIR_StructureMap_Source",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Type or variable this rule applies to.
        "context": FHIR_id,
        # Extensions for context
        "_context": FHIR_Element,
        # Specified minimum cardinality for the element. This is optional; if present, it acts an implicit check on the input content.
        "min": FHIR_integer,
        # Extensions for min
        "_min": FHIR_Element,
        # Specified maximum cardinality for the element - a number or a "*". This is optional; if present, it acts an implicit check on the input content (* just serves as documentation; it's the default value).
        "max": FHIR_string,
        # Extensions for max
        "_max": FHIR_Element,
        # Specified type for the element. This works as a condition on the mapping - use for polymorphic elements.
        "type": FHIR_string,
        # Extensions for type
        "_type": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueBase64Binary": str,
        # Extensions for defaultValueBase64Binary
        "_defaultValueBase64Binary": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueBoolean": bool,
        # Extensions for defaultValueBoolean
        "_defaultValueBoolean": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueCanonical": str,
        # Extensions for defaultValueCanonical
        "_defaultValueCanonical": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueCode": str,
        # Extensions for defaultValueCode
        "_defaultValueCode": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueDate": str,
        # Extensions for defaultValueDate
        "_defaultValueDate": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueDateTime": str,
        # Extensions for defaultValueDateTime
        "_defaultValueDateTime": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueDecimal": float,
        # Extensions for defaultValueDecimal
        "_defaultValueDecimal": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueId": str,
        # Extensions for defaultValueId
        "_defaultValueId": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueInstant": str,
        # Extensions for defaultValueInstant
        "_defaultValueInstant": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueInteger": float,
        # Extensions for defaultValueInteger
        "_defaultValueInteger": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueMarkdown": str,
        # Extensions for defaultValueMarkdown
        "_defaultValueMarkdown": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueOid": str,
        # Extensions for defaultValueOid
        "_defaultValueOid": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValuePositiveInt": float,
        # Extensions for defaultValuePositiveInt
        "_defaultValuePositiveInt": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueString": str,
        # Extensions for defaultValueString
        "_defaultValueString": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueTime": str,
        # Extensions for defaultValueTime
        "_defaultValueTime": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueUnsignedInt": float,
        # Extensions for defaultValueUnsignedInt
        "_defaultValueUnsignedInt": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueUri": str,
        # Extensions for defaultValueUri
        "_defaultValueUri": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueUrl": str,
        # Extensions for defaultValueUrl
        "_defaultValueUrl": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueUuid": str,
        # Extensions for defaultValueUuid
        "_defaultValueUuid": FHIR_Element,
        # A value to use if there is no existing value in the source object.
        "defaultValueAddress": FHIR_Address,
        # A value to use if there is no existing value in the source object.
        "defaultValueAge": FHIR_Age,
        # A value to use if there is no existing value in the source object.
        "defaultValueAnnotation": FHIR_Annotation,
        # A value to use if there is no existing value in the source object.
        "defaultValueAttachment": FHIR_Attachment,
        # A value to use if there is no existing value in the source object.
        "defaultValueCodeableConcept": FHIR_CodeableConcept,
        # A value to use if there is no existing value in the source object.
        "defaultValueCoding": FHIR_Coding,
        # A value to use if there is no existing value in the source object.
        "defaultValueContactPoint": FHIR_ContactPoint,
        # A value to use if there is no existing value in the source object.
        "defaultValueCount": FHIR_Count,
        # A value to use if there is no existing value in the source object.
        "defaultValueDistance": FHIR_Distance,
        # A value to use if there is no existing value in the source object.
        "defaultValueDuration": FHIR_Duration,
        # A value to use if there is no existing value in the source object.
        "defaultValueHumanName": FHIR_HumanName,
        # A value to use if there is no existing value in the source object.
        "defaultValueIdentifier": FHIR_Identifier,
        # A value to use if there is no existing value in the source object.
        "defaultValueMoney": FHIR_Money,
        # A value to use if there is no existing value in the source object.
        "defaultValuePeriod": FHIR_Period,
        # A value to use if there is no existing value in the source object.
        "defaultValueQuantity": FHIR_Quantity,
        # A value to use if there is no existing value in the source object.
        "defaultValueRange": FHIR_Range,
        # A value to use if there is no existing value in the source object.
        "defaultValueRatio": FHIR_Ratio,
        # A value to use if there is no existing value in the source object.
        "defaultValueReference": FHIR_Reference,
        # A value to use if there is no existing value in the source object.
        "defaultValueSampledData": FHIR_SampledData,
        # A value to use if there is no existing value in the source object.
        "defaultValueSignature": FHIR_Signature,
        # A value to use if there is no existing value in the source object.
        "defaultValueTiming": FHIR_Timing,
        # A value to use if there is no existing value in the source object.
        "defaultValueContactDetail": FHIR_ContactDetail,
        # A value to use if there is no existing value in the source object.
        "defaultValueContributor": FHIR_Contributor,
        # A value to use if there is no existing value in the source object.
        "defaultValueDataRequirement": FHIR_DataRequirement,
        # A value to use if there is no existing value in the source object.
        "defaultValueExpression": FHIR_Expression,
        # A value to use if there is no existing value in the source object.
        "defaultValueParameterDefinition": FHIR_ParameterDefinition,
        # A value to use if there is no existing value in the source object.
        "defaultValueRelatedArtifact": FHIR_RelatedArtifact,
        # A value to use if there is no existing value in the source object.
        "defaultValueTriggerDefinition": FHIR_TriggerDefinition,
        # A value to use if there is no existing value in the source object.
        "defaultValueUsageContext": FHIR_UsageContext,
        # A value to use if there is no existing value in the source object.
        "defaultValueDosage": FHIR_Dosage,
        # A value to use if there is no existing value in the source object.
        "defaultValueMeta": FHIR_Meta,
        # Optional field for this source.
        "element": FHIR_string,
        # Extensions for element
        "_element": FHIR_Element,
        # How to handle the list mode for this element.
        "listMode": Literal["first", "not_first", "last", "not_last", "only_one"],
        # Extensions for listMode
        "_listMode": FHIR_Element,
        # Named context for field, if a field is specified.
        "variable": FHIR_id,
        # Extensions for variable
        "_variable": FHIR_Element,
        # FHIRPath expression  - must be true or the rule does not apply.
        "condition": FHIR_string,
        # Extensions for condition
        "_condition": FHIR_Element,
        # FHIRPath expression  - must be true or the mapping engine throws an error instead of completing.
        "check": FHIR_string,
        # Extensions for check
        "_check": FHIR_Element,
        # A FHIRPath expression which specifies a message to put in the transform log when content matching the source rule is found.
        "logMessage": FHIR_string,
        # Extensions for logMessage
        "_logMessage": FHIR_Element,
    },
    total=False,
)
