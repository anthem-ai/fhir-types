from typing import Any, List, Literal, TypedDict

from .FHIR_Annotation import FHIR_Annotation
from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_List_Entry import FHIR_List_Entry
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_uri import FHIR_uri

# A list is a curated collection of resources.
FHIR_List = TypedDict(
    "FHIR_List",
    {
        # This is a List resource
        "resourceType": Literal["List"],
        # The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.
        "id": FHIR_id,
        # The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        "meta": FHIR_Meta,
        # A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.
        "implicitRules": FHIR_uri,
        # Extensions for implicitRules
        "_implicitRules": FHIR_Element,
        # The base language in which the resource is written.
        "language": FHIR_code,
        # Extensions for language
        "_language": FHIR_Element,
        # A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety.
        "text": FHIR_Narrative,
        # These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope.
        "contained": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Identifier for the List assigned for business purposes outside the context of FHIR.
        "identifier": List[FHIR_Identifier],
        # Indicates the current state of this list.
        "status": Literal["current", "retired", "entered-in-error"],
        # Extensions for status
        "_status": FHIR_Element,
        # How this list was prepared - whether it is a working list that is suitable for being maintained on an ongoing basis, or if it represents a snapshot of a list of items from another source, or whether it is a prepared list where items may be marked as added, modified or deleted.
        "mode": Literal["working", "snapshot", "changes"],
        # Extensions for mode
        "_mode": FHIR_Element,
        # A label for the list assigned by the author.
        "title": FHIR_string,
        # Extensions for title
        "_title": FHIR_Element,
        # This code defines the purpose of the list - why it was created.
        "code": FHIR_CodeableConcept,
        # The common subject (or patient) of the resources that are in the list if there is one.
        "subject": FHIR_Reference,
        # The encounter that is the context in which this list was created.
        "encounter": FHIR_Reference,
        # The date that the list was prepared.
        "date": FHIR_dateTime,
        # Extensions for date
        "_date": FHIR_Element,
        # The entity responsible for deciding what the contents of the list were. Where the list was created by a human, this is the same as the author of the list.
        "source": FHIR_Reference,
        # What order applies to the items in the list.
        "orderedBy": FHIR_CodeableConcept,
        # Comments that apply to the overall list.
        "note": List[FHIR_Annotation],
        # Entries in this list.
        "entry": List[FHIR_List_Entry],
        # If the list is empty, why the list is empty.
        "emptyReason": FHIR_CodeableConcept,
    },
    total=False,
)
