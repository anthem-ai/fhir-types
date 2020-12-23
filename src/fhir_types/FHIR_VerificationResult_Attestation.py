from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_date import FHIR_date
from .FHIR_Element import FHIR_Element
from .FHIR_Reference import FHIR_Reference
from .FHIR_Signature import FHIR_Signature
from .FHIR_string import FHIR_string

# Describes validation requirements, source(s), status and dates for one or more elements.
FHIR_VerificationResult_Attestation = TypedDict(
    "FHIR_VerificationResult_Attestation",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The individual or organization attesting to information.
        "who": FHIR_Reference,
        # When the who is asserting on behalf of another (organization or individual).
        "onBehalfOf": FHIR_Reference,
        # The method by which attested information was submitted/retrieved (manual; API; Push).
        "communicationMethod": FHIR_CodeableConcept,
        # The date the information was attested to.
        "date": FHIR_date,
        # Extensions for date
        "_date": FHIR_Element,
        # A digital identity certificate associated with the attestation source.
        "sourceIdentityCertificate": FHIR_string,
        # Extensions for sourceIdentityCertificate
        "_sourceIdentityCertificate": FHIR_Element,
        # A digital identity certificate associated with the proxy entity submitting attested information on behalf of the attestation source.
        "proxyIdentityCertificate": FHIR_string,
        # Extensions for proxyIdentityCertificate
        "_proxyIdentityCertificate": FHIR_Element,
        # Signed assertion by the proxy entity indicating that they have the right to submit attested information on behalf of the attestation source.
        "proxySignature": FHIR_Signature,
        # Signed assertion by the attestation source that they have attested to the information.
        "sourceSignature": FHIR_Signature,
    },
    total=False,
)
