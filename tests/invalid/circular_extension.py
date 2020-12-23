from fhir_types import FHIR_Extension

p: FHIR_Extension = {
    "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
    "valueBoolean": True,
    "valueAddress": {
        "city": "Springfield",
        "QQQstate": "Massachusetts",
        "country": "US",
    },
    "_valueTime": {
        "id": "123",
    },
}
