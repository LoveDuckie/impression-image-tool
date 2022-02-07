#!/bin/bash
<<EOF

   Portfolio \ Setup \ Setup

   Setup the virtual environment required for running the tool (with dependencies)

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CU>RRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

usage() {
   write_info "setup" "usage - setup"
   write_info "setup" "./setup.sh [-? or -h] [-v <virtual environment name>"
   exit 1
}

while getopts ':v:h?' opt; do
   case $opt in
         h|?)
            usage
         ;;
         :)
            write_error "setup" "-${OPTARG} requires an argument"
            usage
         ;;
         *)
            usage
         ;;
   esac
done
