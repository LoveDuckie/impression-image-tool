#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Run \ Format

   Run the formatting tool ("black") on the codebase.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

# Check if Black is installed
if ! command -v black &> /dev/null
then
    write_info "run_format" "Black is not installed. Please install it by running 'pip install black'."
    exit 1
fi

# Check if the user has provided a directory or file as an argument
if [ -z "$1" ]; then
  write_info "run_format" "Usage: $0 <directory-or-file>"
  exit 1
fi

# Run black on the specified directory or file
black $1

# Exit status check
if [ $? -eq 0 ]; then
  write_info "run_format" "Formatting completed successfully!"
else
  write_info "run_format" "Formatting failed. Please check for errors."
  exit 1
fi
write_success "run_format" "Done"
exit 0