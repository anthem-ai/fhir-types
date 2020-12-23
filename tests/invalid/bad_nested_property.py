from fhir_types import FHIR_Patient

p: FHIR_Patient = {
    "resourceType": "Patient",
    "name": [
        {
            "use": "official",
            "family": "Corkery305",
            "givenTTTT": ["Cory323"],
            "prefix": ["Mr."],
        }
    ],
}
