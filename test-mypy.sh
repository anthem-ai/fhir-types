#!/bin/sh

fail() {
    echo "FAIL: $1" >&2
    exit 1
}

# First run mypy on directory to check circular depedencies
mypy src/fhir_types || fail "mypy validation failed, check circular dependecies"

for filename in ./tests/invalid/*.py;
do
  mypy --strict "$filename" && fail "test in failed file $filename"
done

echo "\nShould Succeed Now\n"

for filename in ./tests/valid/*.py;
do
  mypy --strict "$filename" || fail "test in failed file $filename"
done

echo Success
