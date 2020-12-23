# Python Typings For FHIR

The FHIR Types package exports types declared using the [typing](https://docs.python.org/3/library/typing.html) library. This provides type checking support when creating dictionaries of FHIR objects in Python.

## Installation

### Installing from Pypi (recommended)

We recommend you first use a virtual environment and activate it in your shell.

`pip install fhir-types`

### Installing from source
1. Clone this repository
1. Change to the package root directory
1. Run the `pipenv install --dev  --deploy` command to create and install in a virtual environment

```bash
% pipenv install --dev --deploy
Creating a virtualenv for this project...
Pipfile: /fhir-types/Pipfile
Using /usr/local/bin/python3 (3.9.7) to create virtualenv...
. . .
```

If you want to install globally run `pip install .`, outside of a virtual environment.

### Verify the installation

Verify the installation with `pipenv run almake test`.

```bash
% pipenv run almake test
python -m black --check .
All done! ✨ 🍰 ✨
702 files would be left unchanged.
python -m isort --check --df .
. . .
```

Or, if you have `make` installed:

```bash
% pipenv run make test
<same output as shown above>
```

## Usage
This project was developed using [mypy](https://github.com/python/mypy) for type checking.

### Example

Consider these two FHIR JSON dictionaries.

```python
# myfile.py

from fhir_types import FHIR_Patient

# This is a valid patient dictionary
patient: FHIR_Patient = {
    "resourceType": "Patient",
    "gender": "female",
    "name": [
        {
            "use": "official",
            "family": "Johnson",
            "given": ["Jennifer"],
            "prefix": ["Mrs."],
        }
    ]
}

# This is an invalid patient dictionary
invalid_patient: FHIR_Patient = {
    "resourceType": "PPPPatient", # error 1
    "gender": "female123",  # error 2
    "name": [
        {
            "123use": "official", # error 3
            "family": "Johnson",
            "given": ["Jennifer"],
            "prefix": ["Mrs."],
        }
    ]
}
```

After installing `mypy` with `pip`, running `mypy myfile.py` will display the errors in the second (invalid) structure. 

It is good practice to set up your IDE (such as VS Code) to use `mypy` for linting as you work.

## Issues
The Types located in the fhir_types directory are generated from the official `fhir.schema.json` provided by FHIR.

This data stucture is quite large with and contains cyclical relationships. Unfortunately, `mypy` does not handle cyclical relationships and has an open issue [here](https://github.com/python/mypy/issues/731). We added a workaround that reduces the type checking capabilities for certain properties in some classes.

All properties that point to any of the following classes are given an [Any](https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-any-type) type because these lead to circular references. These were found by repeatedly running the `mypy` command.

```bash
CIRCULAR_REFERENCES = {
    "Extension",
    "Identifier",
    "ResourceList",
    "QuestionnaireResponse_Answer",
    "GraphDefinition_Link",
    "ExampleScenario_Process",
    "ExampleScenario_Alternative",
}
```

The other case is when a property points back to a parent class.

```python
from fhir_types import FHIR_Questionnaire_Item

FHIR_Questionnaire_Item = TypedDict("FHIR_Questionnaire_Item", {
    "id": "123",
    item: List[Any] # This used to be FHIR_Questionnaire_Item but was changed to Any
})
```

Here, full type checking can be accomplished by creating two separate dictionaries and then combining them. For example:

```python
from fhir_types import FHIR_Extension, FHIR_Patient

extension: FHIR_Extension = {
    "valueAddress": {
        "city": "Springfield",
        "state": "Massachusetts",
        "country": "US"
    }
}

patient: FHIR_Patient = {
    "gender": "male",
    "extension": [extension]
}
```
