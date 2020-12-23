from typing import Any, List, Literal, TypedDict

from .FHIR_Attachment import FHIR_Attachment
from .FHIR_Element import FHIR_Element
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_integer import FHIR_integer
from .FHIR_string import FHIR_string

# A SubstanceProtein is defined as a single unit of a linear amino acid sequence, or a combination of subunits that are either covalently linked or have a defined invariant stoichiometric relationship. This includes all synthetic, recombinant and purified SubstanceProteins of defined sequence, whether the use is therapeutic or prophylactic. This set of elements will be used to describe albumins, coagulation factors, cytokines, growth factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant vaccines, and immunomodulators.
FHIR_SubstanceProtein_Subunit = TypedDict(
    "FHIR_SubstanceProtein_Subunit",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).
        "modifierExtension": List[Any],
        # Index of primary sequences of amino acids linked through peptide bonds in order of decreasing length. Sequences of the same length will be ordered by molecular weight. Subunits that have identical sequences will be repeated and have sequential subscripts.
        "subunit": FHIR_integer,
        # Extensions for subunit
        "_subunit": FHIR_Element,
        # The sequence information shall be provided enumerating the amino acids from N- to C-terminal end using standard single-letter amino acid codes. Uppercase shall be used for L-amino acids and lowercase for D-amino acids. Transcribed SubstanceProteins will always be described using the translated sequence; for synthetic peptide containing amino acids that are not represented with a single letter code an X should be used within the sequence. The modified amino acids will be distinguished by their position in the sequence.
        "sequence": FHIR_string,
        # Extensions for sequence
        "_sequence": FHIR_Element,
        # Length of linear sequences of amino acids contained in the subunit.
        "length": FHIR_integer,
        # Extensions for length
        "_length": FHIR_Element,
        # The sequence information shall be provided enumerating the amino acids from N- to C-terminal end using standard single-letter amino acid codes. Uppercase shall be used for L-amino acids and lowercase for D-amino acids. Transcribed SubstanceProteins will always be described using the translated sequence; for synthetic peptide containing amino acids that are not represented with a single letter code an X should be used within the sequence. The modified amino acids will be distinguished by their position in the sequence.
        "sequenceAttachment": FHIR_Attachment,
        # Unique identifier for molecular fragment modification based on the ISO 11238 Substance ID.
        "nTerminalModificationId": FHIR_Identifier,
        # The name of the fragment modified at the N-terminal of the SubstanceProtein shall be specified.
        "nTerminalModification": FHIR_string,
        # Extensions for nTerminalModification
        "_nTerminalModification": FHIR_Element,
        # Unique identifier for molecular fragment modification based on the ISO 11238 Substance ID.
        "cTerminalModificationId": FHIR_Identifier,
        # The modification at the C-terminal shall be specified.
        "cTerminalModification": FHIR_string,
        # Extensions for cTerminalModification
        "_cTerminalModification": FHIR_Element,
    },
    total=False,
)
