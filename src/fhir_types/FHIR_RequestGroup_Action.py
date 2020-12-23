from typing import Any, List, Literal, TypedDict

from .FHIR_Age import FHIR_Age
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_Range import FHIR_Range
from .FHIR_Reference import FHIR_Reference
from .FHIR_RelatedArtifact import FHIR_RelatedArtifact
from .FHIR_RequestGroup_Condition import FHIR_RequestGroup_Condition
from .FHIR_RequestGroup_RelatedAction import FHIR_RequestGroup_RelatedAction
from .FHIR_string import FHIR_string
from .FHIR_Timing import FHIR_Timing

# A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
FHIR_RequestGroup_Action = TypedDict(
    "FHIR_RequestGroup_Action",
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
        # A short description of the action used to provide a summary to display to the user.
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
        # A code that provides meaning for the action or action group. For example, a section may have a LOINC code for a section of a documentation template.
        "code": List[FHIR_CodeableConcept],
        # Didactic or other informational resources associated with the action that can be provided to the CDS recipient. Information resources can include inline text commentary and links to web resources.
        "documentation": List[FHIR_RelatedArtifact],
        # An expression that describes applicability criteria, or start/stop conditions for the action.
        "condition": List[FHIR_RequestGroup_Condition],
        # A relationship to another action such as "before" or "30-60 minutes after start of".
        "relatedAction": List[FHIR_RequestGroup_RelatedAction],
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
        # The participant that should perform or be responsible for this action.
        "participant": List[FHIR_Reference],
        # The type of action to perform (create, update, remove).
        "type": FHIR_CodeableConcept,
        # Defines the grouping behavior for the action and its children.
        "groupingBehavior": FHIR_code,
        # Extensions for groupingBehavior
        "_groupingBehavior": FHIR_Element,
        # Defines the selection behavior for the action and its children.
        "selectionBehavior": FHIR_code,
        # Extensions for selectionBehavior
        "_selectionBehavior": FHIR_Element,
        # Defines expectations around whether an action is required.
        "requiredBehavior": FHIR_code,
        # Extensions for requiredBehavior
        "_requiredBehavior": FHIR_Element,
        # Defines whether the action should usually be preselected.
        "precheckBehavior": FHIR_code,
        # Extensions for precheckBehavior
        "_precheckBehavior": FHIR_Element,
        # Defines whether the action can be selected multiple times.
        "cardinalityBehavior": FHIR_code,
        # Extensions for cardinalityBehavior
        "_cardinalityBehavior": FHIR_Element,
        # The resource that is the target of the action (e.g. CommunicationRequest).
        "resource": FHIR_Reference,
        # Sub actions.
        "action": List[Any],
    },
    total=False,
)
