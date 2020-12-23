from typing import Any, List, Literal, TypedDict

from .FHIR_Duration import FHIR_Duration
from .FHIR_Element import FHIR_Element
from .FHIR_MedicationRequest_InitialFill import FHIR_MedicationRequest_InitialFill
from .FHIR_Period import FHIR_Period
from .FHIR_Quantity import FHIR_Quantity
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_unsignedInt import FHIR_unsignedInt

# An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
FHIR_MedicationRequest_DispenseRequest = TypedDict(
    "FHIR_MedicationRequest_DispenseRequest",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Indicates the quantity or duration for the first dispense of the medication.
        "initialFill": FHIR_MedicationRequest_InitialFill,
        # The minimum period of time that must occur between dispenses of the medication.
        "dispenseInterval": FHIR_Duration,
        # This indicates the validity period of a prescription (stale dating the Prescription).
        "validityPeriod": FHIR_Period,
        # An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets.  A prescriber may explicitly say that zero refills are permitted after the initial dispense.
        "numberOfRepeatsAllowed": FHIR_unsignedInt,
        # Extensions for numberOfRepeatsAllowed
        "_numberOfRepeatsAllowed": FHIR_Element,
        # The amount that is to be dispensed for one fill.
        "quantity": FHIR_Quantity,
        # Identifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to last.
        "expectedSupplyDuration": FHIR_Duration,
        # Indicates the intended dispensing Organization specified by the prescriber.
        "performer": FHIR_Reference,
    },
    total=False,
)
