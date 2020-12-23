from fhir_types import FHIR_Extension, FHIR_Patient

ext: FHIR_Extension = {
    "valueAddress": {"city": "Springfield", "state": "Massachusetts", "country": "US"}
}

patient: FHIR_Patient = {"gender": "male", "extension": [ext]}
