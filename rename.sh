#!/usr/bin/env bash
<<EOF

   Tool \ Shell Scripts \ Run \ Rename

   Rename the code files and references to "python-project-template" in the repository.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

export LC_ALL=C
export LC_ALL=en_US.UTF-8

# Function to validate the new project name (alphanumeric with hyphens only)
validate_project_name() {
    if [[ ! "$1" =~ ^[a-zA-Z0-9-]+$ ]]; then
        echo "Error: Project name must be alphanumeric with hyphens only."
        exit 1
    fi
}

# Function to dynamically create hyphenated and underscore versions of the project name
generate_project_names() {
    local base_name="$1"
    old_name_hyphen=$(echo "$base_name" | tr ' ' '-')
    old_name_underscore=$(echo "$base_name" | tr ' ' '_')
    echo "Using pattern '$old_name_hyphen' for hyphenated and '$old_name_underscore' for underscored naming."
}

# Function to recursively rename files and directories
rename_files_and_directories() {
    local new_name="$1"
    local new_name_underscore="${new_name//-/_}" # Convert hyphens to underscores

    # Rename items matching the hyphenated format
    find . -depth -name "*$old_name_hyphen*" | while IFS= read -r item; do
        new_item=$(echo "$item" | sed "s/$old_name_hyphen/$new_name/g")
        echo "Renaming \"$item\" to \"$new_item\""
        mv "$item" "$new_item"
    done

    # Rename items matching the underscored format
    find . -depth -name "*$old_name_underscore*" | while IFS= read -r item; do
        new_item=$(echo "$item" | sed "s/$old_name_underscore/$new_name_underscore/g")
        echo "Renaming \"$item\" to \"$new_item\""
        mv "$item" "$new_item"
    done
}

# Function to replace text inside files
replace_text_in_files() {
    local new_name="$1"
    local new_name_underscore="${new_name//-/_}" # Convert hyphens to underscores

    # Replace occurrences of the hyphenated format in all files
    find . -type f -exec sed -i "s/$old_name_hyphen/$new_name/g" {} \;

    # Replace occurrences of the underscored format in all files
    find . -type f -exec sed -i "s/$old_name_underscore/$new_name_underscore/g" {} \;
}

# Check if a new project name and base project name are provided as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Error: Please provide a new project name and base project name."
    echo "Usage: $0 new-project-name 'base project name'"
    exit 1
else
    new_project_name="$1"
    base_project_name="$2"
fi

# Validate the new project name
validate_project_name "$new_project_name"

# Generate dynamic old names based on the base project name
generate_project_names "$base_project_name"

# Start renaming files and directories
rename_files_and_directories "$new_project_name"

# Replace text within files
replace_text_in_files "$new_project_name"

echo "Renaming and text replacement complete!"
exit 0
