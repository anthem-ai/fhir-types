from typing import Any, List, Literal, TypedDict

from .FHIR_Age import FHIR_Age
from .FHIR_canonical import FHIR_canonical
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_DataRequirement import FHIR_DataRequirement
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Period import FHIR_Period
from .FHIR_PlanDefinition_Condition import FHIR_PlanDefinition_Condition
from .FHIR_PlanDefinition_DynamicValue import FHIR_PlanDefinition_DynamicValue
from .FHIR_PlanDefinition_Participant import FHIR_PlanDefinition_Participant
from .FHIR_PlanDefinition_RelatedAction import FHIR_PlanDefinition_RelatedAction
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing
from .FHIR_TriggerDefinition import FHIR_TriggerDefinition

# This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
FHIR_PlanDefinition_Action = TypedDict(
    "FHIR_PlanDefinition_Action",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # A user-visible prefix for the action.
        "prefix": FHIR_string,
        # Extensions for prefix
        "_prefix": FHIR_Element,
        # The title of the action displayed to a user.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # A brief description of the action used to provide a summary to display to the user.
        "description": FHIR_string,
        # Extensions for description
        "_description": FHIR_Element,
        # A text equivalent of the action to be performed. This provides a human-interpretable description of the action when the definition is consumed by a system that might not be capable of interpreting it dynamically.
        "textEquivalent": FHIR_string,
        # Extensions for textEquivalent
        "_textEquivalent": FHIR_Element,
        # Indicates how quickly the action should be addressed with respect to other actions.
        "priority": FHIR_code,
        # Extensions for priority
        "_priority": FHIR_Element,
        # A code that provides meaning for the action or action group. For example, a section may have a LOINC code for the section of a documentation template.
        "code": List[FHIR_CodeableConcept],
        # A description of why this action is necessary or appropriate.
        "reason": List[FHIR_CodeableConcept],
        # Didactic or other informational resources associated with the action that can be provided to the CDS recipient. Information resources can include inline text commentary and links to web resources.
        "documentation": List[FHIR_RelatedArtifact],
        # Identifies goals that this action supports. The reference must be to a goal element defined within this plan definition.
        "goalId": List[FHIR_id],
        # Extensions for goalId
        "_goalId": List[FHIR_Element],
        # A code or group definition that describes the intended subject of the action and its children, if any.
        "subjectCodeableConcept": FHIR_CodeableConcept,
        # A code or group definition that describes the intended subject of the action and its children, if any.
        "subjectReference": FHIR_Reference,
        # A description of when the action should be triggered.
        "trigger": List[FHIR_TriggerDefinition],
        # An expression that describes applicability criteria or start/stop conditions for the action.
        "condition": List[FHIR_PlanDefinition_Condition],
        # Defines input data requirements for the action.
        "input": List[FHIR_DataRequirement],
        # Defines the outputs of the action, if any.
        "output": List[FHIR_DataRequirement],
        # A relationship to another action such as "before" or "30-60 minutes after start of".
        "relatedAction": List[FHIR_PlanDefinition_RelatedAction],
        # An optional value describing when the action should be performed.
        "timingDateTime": str,
        # Extensions for timingDateTime
        "_timingDateTime": FHIR_Element,
        # An optional value describing when the action should be performed.
        "timingAge": FHIR_Age,
        # An optional value describing when the action should be performed.
        "timingPeriod": FHIR_Period,
        # An optional value describing when the action should be performed.
        "timingDuration": FHIR_Duration,
        # An optional value describing when the action should be performed.
        "timingRange": FHIR_Range,
        # An optional value describing when the action should be performed.
        "timingTiming": FHIR_Timing,
        # Indicates who should participate in performing the action described.
        "participant": List[FHIR_PlanDefinition_Participant],
        # The type of action to perform (create, update, remove).
        "type": FHIR_CodeableConcept,
        # Defines the grouping behavior for the action and its children.
        "groupingBehavior": Literal["visual-group", "logical-group", "sentence-group"],
        # Extensions for groupingBehavior
        "_groupingBehavior": FHIR_Element,
        # Defines the selection behavior for the action and its children.
        "selectionBehavior": Literal[
            "any", "all", "all-or-none", "exactly-one", "at-most-one", "one-or-more"
        ],
        # Extensions for selectionBehavior
        "_selectionBehavior": FHIR_Element,
        # Defines the required behavior for the action.
        "requiredBehavior": Literal["must", "could", "must-unless-documented"],
        # Extensions for requiredBehavior
        "_requiredBehavior": FHIR_Element,
        # Defines whether the action should usually be preselected.
        "precheckBehavior": Literal["yes", "no"],
        # Extensions for precheckBehavior
        "_precheckBehavior": FHIR_Element,
        # Defines whether the action can be selected multiple times.
        "cardinalityBehavior": Literal["single", "multiple"],
        # Extensions for cardinalityBehavior
        "_cardinalityBehavior": FHIR_Element,
        # A reference to an ActivityDefinition that describes the action to be taken in detail, or a PlanDefinition that describes a series of actions to be taken.
        "definitionCanonical": str,
        # Extensions for definitionCanonical
        "_definitionCanonical": FHIR_Element,
        # A reference to an ActivityDefinition that describes the action to be taken in detail, or a PlanDefinition that describes a series of actions to be taken.
        "definitionUri": str,
        # Extensions for definitionUri
        "_definitionUri": FHIR_Element,
        # A reference to a StructureMap resource that defines a transform that can be executed to produce the intent resource using the ActivityDefinition instance as the input.
        "transform": FHIR_canonical,
        # Customizations that should be applied to the statically defined resource. For example, if the dosage of a medication must be computed based on the patient's weight, a customization would be used to specify an expression that calculated the weight, and the path on the resource that would contain the result.
        "dynamicValue": List[FHIR_PlanDefinition_DynamicValue],
        # Sub actions that are contained within the action. The behavior of this action determines the functionality of the sub-actions. For example, a selection behavior of at-most-one indicates that of the sub-actions, at most one may be chosen as part of realizing the action definition.
        "action": List[Any],
    },
    total=False,
)
