from typing import Any, List, Literal, TypedDict

from .FHIR_boolean import FHIR_boolean
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_DataRequirement import FHIR_DataRequirement
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_Expression import FHIR_Expression
from .FHIR_Period import FHIR_Period
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_TriggerDefinition import FHIR_TriggerDefinition
from .FHIR_UsageContext import FHIR_UsageContext

# The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
FHIR_EvidenceVariable_Characteristic = TypedDict(
    "FHIR_EvidenceVariable_Characteristic",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A short, natural language description of the characteristic that could be used to communicate the criteria to an end-user.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionReference": FHIR_Reference,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionCanonical": str,
        # Extensions for definitionCanonical
        "_definitionCanonical": FHIR_Element,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionCodeableConcept": FHIR_CodeableConcept,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionExpression": FHIR_Expression,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionDataRequirement": FHIR_DataRequirement,
        # Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).
        "definitionTriggerDefinition": FHIR_TriggerDefinition,
        # Use UsageContext to define the members of the population, such as Age Ranges, Genders, Settings.
        "usageContext": List[FHIR_UsageContext],
        # When true, members with this characteristic are excluded from the element.
        "exclude": FHIR_boolean,
        # Extensions for exclude
        "_exclude": FHIR_Element,
        # Indicates what effective period the study covers.
        "participantEffectiveDateTime": str,
        # Extensions for participantEffectiveDateTime
        "_participantEffectiveDateTime": FHIR_Element,
        # Indicates what effective period the study covers.
        "participantEffectivePeriod": FHIR_Period,
        # Indicates what effective period the study covers.
        "participantEffectiveDuration": FHIR_Duration,
        # Indicates what effective period the study covers.
        "participantEffectiveTiming": FHIR_Timing,
        # Indicates duration from the participant's study entry.
        "timeFromStart": FHIR_Duration,
        # Indicates how elements are aggregated within the study effective period.
        "groupMeasure": Literal[
            "mean",
            "median",
            "mean-of-mean",
            "mean-of-median",
            "median-of-mean",
            "median-of-median",
        ],
        # Extensions for groupMeasure
        "_groupMeasure": FHIR_Element,
    },
    total=False,
)
