# Tests

Tests are written for pytest

Run all tests...

    pytest smpa

Run all tests but stop when the first one fails...

    pytest -x smpa

Run all tests with log / print output...

    pytest -s smpa

Run all tests with log / print output but stop when the first one fails...

    pytest -xs smpa

Run all tests and drop into a debugger if any fail.

    pytest --pdb smpa


## Test Coverage

To generate a coverage report while running the tests...

    pytest smpa --cov=smpa


To send the coverage report to Codacy, requires `$CODACY_PROJECT_TOKEN` (currently stored in EnvKey) in your shell environment and the `codacy-coverage` package installed on your local machine.

In the container's shell...

    coverage xml

On your local machine...

    python-codacy-coverage -r app/coverage.xml

To get a local HTML coverage report...

    pytest smpa --cov=smpa --cov-report html:coverage
