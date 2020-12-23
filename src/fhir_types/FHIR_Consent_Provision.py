from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Coding import FHIR_Coding
from .FHIR_Consent_Actor import FHIR_Consent_Actor
from .FHIR_Consent_Data import FHIR_Consent_Data
from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string

# A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
FHIR_Consent_Provision = TypedDict(
    "FHIR_Consent_Provision",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.
        "type": Literal["deny", "permit"],
        # Extensions for type
        "_type": FHIR_Element,
        # The timeframe in this rule is valid.
        "period": FHIR_Period,
        # Who or what is controlled by this rule. Use group to identify a set of actors by some property they share (e.g. 'admitting officers').
        "actor": List[FHIR_Consent_Actor],
        # Actions controlled by this Rule.
        "action": List[FHIR_CodeableConcept],
        # A security label, comprised of 0..* security label fields (Privacy tags), which define which resources are controlled by this exception.
        "securityLabel": List[FHIR_Coding],
        # The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.
        "purpose": List[FHIR_Coding],
        # The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.
        "class": List[FHIR_Coding],
        # If this code is found in an instance, then the rule applies.
        "code": List[FHIR_CodeableConcept],
        # Clinical or Operational Relevant period of time that bounds the data controlled by this rule.
        "dataPeriod": FHIR_Period,
        # The resources controlled by this rule if specific resources are referenced.
        "data": List[FHIR_Consent_Data],
        # Rules which provide exceptions to the base rule or subrules.
        "provision": List[Any],
    },
    total=False,
)
