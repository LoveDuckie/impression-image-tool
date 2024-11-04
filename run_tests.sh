#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Run \ Tests

   Run the unit tests discovered in the codebase.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

# Check if coverage is installed
if ! command -v coverage &> /dev/null
then
    echo "Coverage is not installed. Please install it by running 'pip install coverage'."
    exit 1
fi

# Check if the user provided a directory or file to test
if [ -z "$1" ]; then
    write_info "run_tests" "Usage: $0 <test-directory-or-file>"
    exit 1
fi

# Run the unit tests with coverage
poetry run coverage run --source=. -m unittest discover -s $1

# Check if the tests passed
if [ $? -eq 0 ]; then
    write_info "run_tests" "Unit tests passed."
else
    write_error "run_tests" "Some unit tests failed. Please review the errors."
    exit 1
fi

# Generate coverage report
write_info "run_tests" "Generating coverage report..."
coverage report -m
coverage html

write_info "run_tests" "Coverage report generated. Open 'htmlcov/index.html' to view the detailed report."

write_success "run_tests" "Done"
exit 0