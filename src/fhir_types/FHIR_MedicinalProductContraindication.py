from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_MedicinalProductContraindication_OtherTherapy import (
    FHIR_MedicinalProductContraindication_OtherTherapy,
)
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Population import FHIR_Population
from .FHIR_Reference import FHIR_Reference
from .FHIR_uri import FHIR_uri

# The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.
FHIR_MedicinalProductContraindication = TypedDict(
    "FHIR_MedicinalProductContraindication",
    {
        # This is a MedicinalProductContraindication resource
        "resourceType": Literal["MedicinalProductContraindication"],
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
        # The medication for which this is an indication.
        "subject": List[FHIR_Reference],
        # The disease, symptom or procedure for the contraindication.
        "disease": FHIR_CodeableConcept,
        # The status of the disease or symptom for the contraindication.
        "diseaseStatus": FHIR_CodeableConcept,
        # A comorbidity (concurrent condition) or coinfection.
        "comorbidity": List[FHIR_CodeableConcept],
        # Information about the use of the medicinal product in relation to other therapies as part of the indication.
        "therapeuticIndication": List[FHIR_Reference],
        # Information about the use of the medicinal product in relation to other therapies described as part of the indication.
        "otherTherapy": List[FHIR_MedicinalProductContraindication_OtherTherapy],
        # The population group to which this applies.
        "population": List[FHIR_Population],
    },
    total=False,
)
