#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Run \ Lint

   Run the linting tool on the codebase.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

# Check if pylint is installed
if ! command -v pylint &> /dev/null
then
    write_error "run_lint" "Pylint is not installed. Please install it by running 'pip install pylint'."
    exit 1
fi

# Check if the user has provided a directory or file to lint
if [ -z "$1" ]; then
    write_error "run_lint" "Usage: $0 <directory-or-file>"
    exit 1
fi

# Run pylint on the specified directory or file
pylint $1

# Check if pylint completed successfully
if [ $? -eq 0 ]; then
    write_info "run_lint" "Pylint completed without any errors!"
else
    write_info "run_lint" "Pylint detected issues. Please review the output for details."
    exit 1
fi

write_success "run_lint" "Done"
exit 0