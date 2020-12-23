fhir.schema.json.zip:
	curl -O https://www.hl7.org/fhir/fhir.schema.json.zip

fhir.schema.json:
	$(MAKE) fhir.jsonschema.json.zip # This file is .gitignored
	unzip fhir.schema.json.zip
	test -f fhir.schema.json && touch fhir.schema.json # This target is ran every time without updating the mtime

format:
	python -m black --quiet .
	python -m isort --quiet .

generate-fhir:
	python ./scripts/generate.py

generate: generate-fhir
	$(MAKE) format

test-formatting:
	python -m black --check .
	python -m isort --check --df .

test-lint:
	python -m pflake8 scripts
	python -m pflake8 --ignore E501,E721 tests

test-mypy:
	sh test-mypy.sh

test-scripts:
	python -m pytest --cov=scripts --cov-report=term --cov-fail-under=90 --durations=3

test: test-formatting test-lint test-scripts test-mypy

servedocs:
	pdoc fhir_types

build-dist:
	# Remove old dist files, if present.
	rm dist/* || true
	# Reproducible wheel build by setting SOURCE_DATE_EPOCH
	# https://github.com/kushaldas/asaman/blob/ae82002dccb1ab7a97e3bb543d0e09c397c402b1/asaman/__init__.py#L18
	SOURCE_DATE_EPOCH=1309379017 python -m build --no-isolation
	# Let twine validate the sdist and wheel
	python -m twine check --strict dist/*

publish: build-dist
	python -m twine upload dist/*
