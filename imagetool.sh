#!/bin/bash
<<EOF

   Portfolio \ Tools \ Python \ Impression Image Tool

   A simple bootstrap script responsible for running the impression image tool, and
   ensuring that the virtual environment is created and provisioned

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/../../../Docker/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

PYTHON_VIRTUALENV_PATH=$CURRENT_DIRECTORY/venv

write_success "imagetool" "done"