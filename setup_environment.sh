#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Setup \ Poetry Environment

   A simple script for setting up the Poetry development environment

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

if ! is_command_available poetry; then
    write_error "setup_environment" "Failed: \"poetry\" was not found on this system."
    exit 1
fi
if ! is_command_available pyenv; then
    write_error "setup_environment" "Failed: \"pyenv\" was not found on this system."
    exit 2
fi

poetry env remove --all
poetry env use
poetry install

write_success "setup_environment" "Done"