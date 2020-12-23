from typing import Any, List, Literal, TypedDict

from .FHIR_CodeableConcept import FHIR_CodeableConcept
from .FHIR_Element import FHIR_Element
from .FHIR_string import FHIR_string
from .FHIR_SubstanceSourceMaterial_Author import FHIR_SubstanceSourceMaterial_Author
from .FHIR_SubstanceSourceMaterial_Hybrid import FHIR_SubstanceSourceMaterial_Hybrid
from .FHIR_SubstanceSourceMaterial_OrganismGeneral import (
    FHIR_SubstanceSourceMaterial_OrganismGeneral,
)

# Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
FHIR_SubstanceSourceMaterial_Organism = TypedDict(
    "FHIR_SubstanceSourceMaterial_Organism",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # The family of an organism shall be specified.
        "family": FHIR_CodeableConcept,
        # The genus of an organism shall be specified; refers to the Latin epithet of the genus element of the plant/animal scientific name; it is present in names for genera, species and infraspecies.
        "genus": FHIR_CodeableConcept,
        # The species of an organism shall be specified; refers to the Latin epithet of the species of the plant/animal; it is present in names for species and infraspecies.
        "species": FHIR_CodeableConcept,
        # The Intraspecific type of an organism shall be specified.
        "intraspecificType": FHIR_CodeableConcept,
        # The intraspecific description of an organism shall be specified based on a controlled vocabulary. For Influenza Vaccine, the intraspecific description shall contain the syntax of the antigen in line with the WHO convention.
        "intraspecificDescription": FHIR_string,
        # Extensions for intraspecificDescription
        "_intraspecificDescription": FHIR_Element,
        # 4.9.13.6.1 Author type (Conditional).
        "author": List[FHIR_SubstanceSourceMaterial_Author],
        # 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
        "hybrid": FHIR_SubstanceSourceMaterial_Hybrid,
        # 4.9.13.7.1 Kingdom (Conditional).
        "organismGeneral": FHIR_SubstanceSourceMaterial_OrganismGeneral,
    },
    total=False,
)
