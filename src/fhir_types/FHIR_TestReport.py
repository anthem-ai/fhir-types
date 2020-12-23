from typing import Any, List, Literal, TypedDict

from .FHIR_code import FHIR_code
from .FHIR_dateTime import FHIR_dateTime
from .FHIR_decimal import FHIR_decimal
from .FHIR_Element import FHIR_Element
from .FHIR_id import FHIR_id
from .FHIR_Identifier import FHIR_Identifier
from .FHIR_Meta import FHIR_Meta
from .FHIR_Narrative import FHIR_Narrative
from .FHIR_Reference import FHIR_Reference
from .FHIR_string import FHIR_string
from .FHIR_TestReport_Participant import FHIR_TestReport_Participant
from .FHIR_TestReport_Setup import FHIR_TestReport_Setup
from .FHIR_TestReport_Teardown import FHIR_TestReport_Teardown
from .FHIR_TestReport_Test import FHIR_TestReport_Test
from .FHIR_uri import FHIR_uri

# A summary of information based on the results of executing a TestScript.
FHIR_TestReport = TypedDict(
    "FHIR_TestReport",
    {
        # This is a TestReport resource
        "resourceType": Literal["TestReport"],
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
        # Identifier for the TestScript assigned for external purposes outside the context of FHIR.
        "identifier": FHIR_Identifier,
        # A free text natural language name identifying the executed TestScript.
        "name": FHIR_string,
        # Extensions for name
        "_name": FHIR_Element,
        # The current state of this test report.
        "status": Literal[
            "completed", "in-progress", "waiting", "stopped", "entered-in-error"
        ],
        # Extensions for status
        "_status": FHIR_Element,
        # Ideally this is an absolute URL that is used to identify the version-specific TestScript that was executed, matching the `TestScript.url`.
        "testScript": FHIR_Reference,
        # The overall result from the execution of the TestScript.
        "result": Literal["pass", "fail", "pending"],
        # Extensions for result
        "_result": FHIR_Element,
        # The final score (percentage of tests passed) resulting from the execution of the TestScript.
        "score": FHIR_decimal,
        # Extensions for score
        "_score": FHIR_Element,
        # Name of the tester producing this report (Organization or individual).
        "tester": FHIR_string,
        # Extensions for tester
        "_tester": FHIR_Element,
        # When the TestScript was executed and this TestReport was generated.
        "issued": FHIR_dateTime,
        # Extensions for issued
        "_issued": FHIR_Element,
        # A participant in the test execution, either the execution engine, a client, or a server.
        "participant": List[FHIR_TestReport_Participant],
        # The results of the series of required setup operations before the tests were executed.
        "setup": FHIR_TestReport_Setup,
        # A test executed from the test script.
        "test": List[FHIR_TestReport_Test],
        # The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise).
        "teardown": FHIR_TestReport_Teardown,
    },
    total=False,
)
