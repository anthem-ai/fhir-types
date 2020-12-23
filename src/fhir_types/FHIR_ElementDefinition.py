from typing import Any, List, Literal, TypedDict

from .FHIR_Address import FHIR_Address
from .FHIR_Age import FHIR_Age
from .FHIR_Annotation import FHIR_Annotation
from .FHIR_Attachment import FHIR_Attachment
from .FHIR_boolean import FHIR_boolean
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
from .FHIR_ElementDefinition_Base import FHIR_ElementDefinition_Base
from .FHIR_ElementDefinition_Binding import FHIR_ElementDefinition_Binding
from .FHIR_ElementDefinition_Constraint import FHIR_ElementDefinition_Constraint
from .FHIR_ElementDefinition_Example import FHIR_ElementDefinition_Example
from .FHIR_ElementDefinition_Mapping import FHIR_ElementDefinition_Mapping
from .FHIR_ElementDefinition_Slicing import FHIR_ElementDefinition_Slicing
from .FHIR_ElementDefinition_Type import FHIR_ElementDefinition_Type
from .FHIR_Expression import FHIR_Expression
from .FHIR_HumanName import FHIR_HumanName
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_integer import FHIR_integer
from .FHIR_markdown import FHIR_markdown
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
from .FHIR_unsignedInt import FHIR_unsignedInt
from .FHIR_uri import FHIR_uri
from .FHIR_UsageContext import FHIR_UsageContext

# Captures constraints on each element within the resource, profile, or extension.
FHIR_ElementDefinition = TypedDict(
    "FHIR_ElementDefinition",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The path identifies the element and is expressed as a "."-separated list of ancestor elements, beginning with the name of the resource or extension.
        "path": FHIR_string,
        # Extensions for path
        "_path": FHIR_Element,
        # Codes that define how this element is represented in instances, when the deviation varies from the normal case.
        "representation": List[
            Literal["xmlAttr", "xmlText", "typeAttr", "cdaText", "xhtml"]
        ],
        # Extensions for representation
        "_representation": List[FHIR_Element],
        # The name of this element definition slice, when slicing is working. The name must be a token with no dots or spaces. This is a unique name referring to a specific set of constraints applied to this element, used to provide a name to different slices of the same element.
        "sliceName": FHIR_string,
        # Extensions for sliceName
        "_sliceName": FHIR_Element,
        # If true, indicates that this slice definition is constraining a slice definition with the same name in an inherited profile. If false, the slice is not overriding any slice in an inherited profile. If missing, the slice might or might not be overriding a slice in an inherited profile, depending on the sliceName.
        "sliceIsConstraining": FHIR_boolean,
        # Extensions for sliceIsConstraining
        "_sliceIsConstraining": FHIR_Element,
        # A single preferred label which is the text to display beside the element indicating its meaning or to use to prompt for the element in a user display or form.
        "label": FHIR_string,
        # Extensions for label
        "_label": FHIR_Element,
        # A code that has the same meaning as the element in a particular terminology.
        "code": List[FHIR_Coding],
        # Indicates that the element is sliced into a set of alternative definitions (i.e. in a structure definition, there are multiple different constraints on a single element in the base resource). Slicing can be used in any resource that has cardinality ..* on the base resource, or any resource with a choice of types. The set of slices is any elements that come after this in the element sequence that have the same path, until a shorter path occurs (the shorter path terminates the set).
        "slicing": FHIR_ElementDefinition_Slicing,
        # A concise description of what this element means (e.g. for use in autogenerated summaries).
        "short": FHIR_string,
        # Extensions for short
        "_short": FHIR_Element,
        # Provides a complete explanation of the meaning of the data element for human readability.  For the case of elements derived from existing elements (e.g. constraints), the definition SHALL be consistent with the base definition, but convey the meaning of the element in the particular context of use of the resource. (Note: The text you are reading is specified in ElementDefinition.definition).
        "definition": FHIR_markdown,
        # Extensions for definition
        "_definition": FHIR_Element,
        # Explanatory notes and implementation guidance about the data element, including notes about how to use the data properly, exceptions to proper use, etc. (Note: The text you are reading is specified in ElementDefinition.comment).
        "comment": FHIR_markdown,
        # Extensions for comment
        "_comment": FHIR_Element,
        # This element is for traceability of why the element was created and why the constraints exist as they do. This may be used to point to source materials or specifications that drove the structure of this element.
        "requirements": FHIR_markdown,
        # Extensions for requirements
        "_requirements": FHIR_Element,
        # Identifies additional names by which this element might also be known.
        "alias": List[FHIR_string],
        # Extensions for alias
        "_alias": List[FHIR_Element],
        # The minimum number of times this element SHALL appear in the instance.
        "min": FHIR_unsignedInt,
        # Extensions for min
        "_min": FHIR_Element,
        # The maximum number of times this element is permitted to appear in the instance.
        "max": FHIR_string,
        # Extensions for max
        "_max": FHIR_Element,
        # Information about the base definition of the element, provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles. When the element definition is not the original definition of an element - i.g. either in a constraint on another type, or for elements from a super type in a snap shot - then the information in provided in the element definition may be different to the base definition. On the original definition of the element, it will be same.
        "base": FHIR_ElementDefinition_Base,
        # Identifies an element defined elsewhere in the definition whose content rules should be applied to the current element. ContentReferences bring across all the rules that are in the ElementDefinition for the element, including definitions, cardinality constraints, bindings, invariants etc.
        "contentReference": FHIR_uri,
        # Extensions for contentReference
        "_contentReference": FHIR_Element,
        # The data type or resource that the value of this element is permitted to be.
        "type": List[FHIR_ElementDefinition_Type],
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueBase64Binary": str,
        # Extensions for defaultValueBase64Binary
        "_defaultValueBase64Binary": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueBoolean": bool,
        # Extensions for defaultValueBoolean
        "_defaultValueBoolean": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueCanonical": str,
        # Extensions for defaultValueCanonical
        "_defaultValueCanonical": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueCode": str,
        # Extensions for defaultValueCode
        "_defaultValueCode": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDate": str,
        # Extensions for defaultValueDate
        "_defaultValueDate": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDateTime": str,
        # Extensions for defaultValueDateTime
        "_defaultValueDateTime": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDecimal": float,
        # Extensions for defaultValueDecimal
        "_defaultValueDecimal": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueId": str,
        # Extensions for defaultValueId
        "_defaultValueId": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueInstant": str,
        # Extensions for defaultValueInstant
        "_defaultValueInstant": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueInteger": float,
        # Extensions for defaultValueInteger
        "_defaultValueInteger": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueMarkdown": str,
        # Extensions for defaultValueMarkdown
        "_defaultValueMarkdown": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueOid": str,
        # Extensions for defaultValueOid
        "_defaultValueOid": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValuePositiveInt": float,
        # Extensions for defaultValuePositiveInt
        "_defaultValuePositiveInt": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueString": str,
        # Extensions for defaultValueString
        "_defaultValueString": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueTime": str,
        # Extensions for defaultValueTime
        "_defaultValueTime": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueUnsignedInt": float,
        # Extensions for defaultValueUnsignedInt
        "_defaultValueUnsignedInt": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueUri": str,
        # Extensions for defaultValueUri
        "_defaultValueUri": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueUrl": str,
        # Extensions for defaultValueUrl
        "_defaultValueUrl": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueUuid": str,
        # Extensions for defaultValueUuid
        "_defaultValueUuid": FHIR_Element,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueAddress": FHIR_Address,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueAge": FHIR_Age,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueAnnotation": FHIR_Annotation,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueAttachment": FHIR_Attachment,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueCodeableConcept": FHIR_CodeableConcept,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueCoding": FHIR_Coding,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueContactPoint": FHIR_ContactPoint,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueCount": FHIR_Count,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDistance": FHIR_Distance,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDuration": FHIR_Duration,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueHumanName": FHIR_HumanName,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueIdentifier": FHIR_Identifier,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueMoney": FHIR_Money,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValuePeriod": FHIR_Period,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueQuantity": FHIR_Quantity,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueRange": FHIR_Range,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueRatio": FHIR_Ratio,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueReference": FHIR_Reference,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueSampledData": FHIR_SampledData,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueSignature": FHIR_Signature,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueTiming": FHIR_Timing,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueContactDetail": FHIR_ContactDetail,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueContributor": FHIR_Contributor,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDataRequirement": FHIR_DataRequirement,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueExpression": FHIR_Expression,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueParameterDefinition": FHIR_ParameterDefinition,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueRelatedArtifact": FHIR_RelatedArtifact,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueTriggerDefinition": FHIR_TriggerDefinition,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueUsageContext": FHIR_UsageContext,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueDosage": FHIR_Dosage,
        # The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').
        "defaultValueMeta": FHIR_Meta,
        # The Implicit meaning that is to be understood when this element is missing (e.g. 'when this element is missing, the period is ongoing').
        "meaningWhenMissing": FHIR_markdown,
        # Extensions for meaningWhenMissing
        "_meaningWhenMissing": FHIR_Element,
        # If present, indicates that the order of the repeating element has meaning and describes what that meaning is.  If absent, it means that the order of the element has no meaning.
        "orderMeaning": FHIR_string,
        # Extensions for orderMeaning
        "_orderMeaning": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedBase64Binary": str,
        # Extensions for fixedBase64Binary
        "_fixedBase64Binary": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedBoolean": bool,
        # Extensions for fixedBoolean
        "_fixedBoolean": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedCanonical": str,
        # Extensions for fixedCanonical
        "_fixedCanonical": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedCode": str,
        # Extensions for fixedCode
        "_fixedCode": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDate": str,
        # Extensions for fixedDate
        "_fixedDate": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDateTime": str,
        # Extensions for fixedDateTime
        "_fixedDateTime": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDecimal": float,
        # Extensions for fixedDecimal
        "_fixedDecimal": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedId": str,
        # Extensions for fixedId
        "_fixedId": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedInstant": str,
        # Extensions for fixedInstant
        "_fixedInstant": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedInteger": float,
        # Extensions for fixedInteger
        "_fixedInteger": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedMarkdown": str,
        # Extensions for fixedMarkdown
        "_fixedMarkdown": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedOid": str,
        # Extensions for fixedOid
        "_fixedOid": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedPositiveInt": float,
        # Extensions for fixedPositiveInt
        "_fixedPositiveInt": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedString": str,
        # Extensions for fixedString
        "_fixedString": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedTime": str,
        # Extensions for fixedTime
        "_fixedTime": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedUnsignedInt": float,
        # Extensions for fixedUnsignedInt
        "_fixedUnsignedInt": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedUri": str,
        # Extensions for fixedUri
        "_fixedUri": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedUrl": str,
        # Extensions for fixedUrl
        "_fixedUrl": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedUuid": str,
        # Extensions for fixedUuid
        "_fixedUuid": FHIR_Element,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedAddress": FHIR_Address,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedAge": FHIR_Age,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedAnnotation": FHIR_Annotation,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedAttachment": FHIR_Attachment,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedCodeableConcept": FHIR_CodeableConcept,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedCoding": FHIR_Coding,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedContactPoint": FHIR_ContactPoint,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedCount": FHIR_Count,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDistance": FHIR_Distance,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDuration": FHIR_Duration,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedHumanName": FHIR_HumanName,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedIdentifier": FHIR_Identifier,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedMoney": FHIR_Money,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedPeriod": FHIR_Period,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedQuantity": FHIR_Quantity,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedRange": FHIR_Range,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedRatio": FHIR_Ratio,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedReference": FHIR_Reference,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedSampledData": FHIR_SampledData,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedSignature": FHIR_Signature,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedTiming": FHIR_Timing,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedContactDetail": FHIR_ContactDetail,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedContributor": FHIR_Contributor,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDataRequirement": FHIR_DataRequirement,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedExpression": FHIR_Expression,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedParameterDefinition": FHIR_ParameterDefinition,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedRelatedArtifact": FHIR_RelatedArtifact,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedTriggerDefinition": FHIR_TriggerDefinition,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedUsageContext": FHIR_UsageContext,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedDosage": FHIR_Dosage,
        # Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.
        "fixedMeta": FHIR_Meta,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternBase64Binary": str,
        # Extensions for patternBase64Binary
        "_patternBase64Binary": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternBoolean": bool,
        # Extensions for patternBoolean
        "_patternBoolean": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternCanonical": str,
        # Extensions for patternCanonical
        "_patternCanonical": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternCode": str,
        # Extensions for patternCode
        "_patternCode": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDate": str,
        # Extensions for patternDate
        "_patternDate": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDateTime": str,
        # Extensions for patternDateTime
        "_patternDateTime": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDecimal": float,
        # Extensions for patternDecimal
        "_patternDecimal": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternId": str,
        # Extensions for patternId
        "_patternId": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternInstant": str,
        # Extensions for patternInstant
        "_patternInstant": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternInteger": float,
        # Extensions for patternInteger
        "_patternInteger": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternMarkdown": str,
        # Extensions for patternMarkdown
        "_patternMarkdown": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternOid": str,
        # Extensions for patternOid
        "_patternOid": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternPositiveInt": float,
        # Extensions for patternPositiveInt
        "_patternPositiveInt": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternString": str,
        # Extensions for patternString
        "_patternString": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternTime": str,
        # Extensions for patternTime
        "_patternTime": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternUnsignedInt": float,
        # Extensions for patternUnsignedInt
        "_patternUnsignedInt": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternUri": str,
        # Extensions for patternUri
        "_patternUri": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternUrl": str,
        # Extensions for patternUrl
        "_patternUrl": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternUuid": str,
        # Extensions for patternUuid
        "_patternUuid": FHIR_Element,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternAddress": FHIR_Address,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternAge": FHIR_Age,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternAnnotation": FHIR_Annotation,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternAttachment": FHIR_Attachment,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternCodeableConcept": FHIR_CodeableConcept,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternCoding": FHIR_Coding,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternContactPoint": FHIR_ContactPoint,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternCount": FHIR_Count,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDistance": FHIR_Distance,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDuration": FHIR_Duration,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternHumanName": FHIR_HumanName,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternIdentifier": FHIR_Identifier,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternMoney": FHIR_Money,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternPeriod": FHIR_Period,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternQuantity": FHIR_Quantity,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternRange": FHIR_Range,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternRatio": FHIR_Ratio,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternReference": FHIR_Reference,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternSampledData": FHIR_SampledData,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternSignature": FHIR_Signature,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternTiming": FHIR_Timing,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternContactDetail": FHIR_ContactDetail,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternContributor": FHIR_Contributor,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDataRequirement": FHIR_DataRequirement,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternExpression": FHIR_Expression,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternParameterDefinition": FHIR_ParameterDefinition,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternRelatedArtifact": FHIR_RelatedArtifact,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternTriggerDefinition": FHIR_TriggerDefinition,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternUsageContext": FHIR_UsageContext,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternDosage": FHIR_Dosage,
        # Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.  When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,1. If primitive: it must match exactly the pattern value2. If a complex object: it must match (recursively) the pattern value3. If an array: it must match (recursively) the pattern value.
        "patternMeta": FHIR_Meta,
        # A sample value for this element demonstrating the type of information that would typically be found in the element.
        "example": List[FHIR_ElementDefinition_Example],
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueDate": str,
        # Extensions for minValueDate
        "_minValueDate": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueDateTime": str,
        # Extensions for minValueDateTime
        "_minValueDateTime": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueInstant": str,
        # Extensions for minValueInstant
        "_minValueInstant": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueTime": str,
        # Extensions for minValueTime
        "_minValueTime": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueDecimal": float,
        # Extensions for minValueDecimal
        "_minValueDecimal": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueInteger": float,
        # Extensions for minValueInteger
        "_minValueInteger": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValuePositiveInt": float,
        # Extensions for minValuePositiveInt
        "_minValuePositiveInt": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueUnsignedInt": float,
        # Extensions for minValueUnsignedInt
        "_minValueUnsignedInt": FHIR_Element,
        # The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "minValueQuantity": FHIR_Quantity,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueDate": str,
        # Extensions for maxValueDate
        "_maxValueDate": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueDateTime": str,
        # Extensions for maxValueDateTime
        "_maxValueDateTime": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueInstant": str,
        # Extensions for maxValueInstant
        "_maxValueInstant": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueTime": str,
        # Extensions for maxValueTime
        "_maxValueTime": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueDecimal": float,
        # Extensions for maxValueDecimal
        "_maxValueDecimal": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueInteger": float,
        # Extensions for maxValueInteger
        "_maxValueInteger": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValuePositiveInt": float,
        # Extensions for maxValuePositiveInt
        "_maxValuePositiveInt": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueUnsignedInt": float,
        # Extensions for maxValueUnsignedInt
        "_maxValueUnsignedInt": FHIR_Element,
        # The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.
        "maxValueQuantity": FHIR_Quantity,
        # Indicates the maximum length in characters that is permitted to be present in conformant instances and which is expected to be supported by conformant consumers that support the element.
        "maxLength": FHIR_integer,
        # Extensions for maxLength
        "_maxLength": FHIR_Element,
        # A reference to an invariant that may make additional statements about the cardinality or value in the instance.
        "condition": List[FHIR_id],
        # Extensions for condition
        "_condition": List[FHIR_Element],
        # Formal constraints such as co-occurrence and other constraints that can be computationally evaluated within the context of the instance.
        "constraint": List[FHIR_ElementDefinition_Constraint],
        # If true, implementations that produce or consume resources SHALL provide "support" for the element in some meaningful way.  If false, the element may be ignored and not supported. If false, whether to populate or use the data element in any way is at the discretion of the implementation.
        "mustSupport": FHIR_boolean,
        # Extensions for mustSupport
        "_mustSupport": FHIR_Element,
        # If true, the value of this element affects the interpretation of the element or resource that contains it, and the value of the element cannot be ignored. Typically, this is used for status, negation and qualification codes. The effect of this is that the element cannot be ignored by systems: they SHALL either recognize the element and process it, and/or a pre-determination has been made that it is not relevant to their particular system.
        "isModifier": FHIR_boolean,
        # Extensions for isModifier
        "_isModifier": FHIR_Element,
        # Explains how that element affects the interpretation of the resource or element that contains it.
        "isModifierReason": FHIR_string,
        # Extensions for isModifierReason
        "_isModifierReason": FHIR_Element,
        # Whether the element should be included if a client requests a search with the parameter _summary=true.
        "isSummary": FHIR_boolean,
        # Extensions for isSummary
        "_isSummary": FHIR_Element,
        # Binds to a value set if this element is coded (code, Coding, CodeableConcept, Quantity), or the data types (string, uri).
        "binding": FHIR_ElementDefinition_Binding,
        # Identifies a concept from an external specification that roughly corresponds to this element.
        "mapping": List[FHIR_ElementDefinition_Mapping],
    },
    total=False,
)
