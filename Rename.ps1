#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Tool \ PowerShell Scripts \ Run \ Rename

    Rename the code files and references to "python-project-template" in the repository.
#>

# Get the current script directory and file details
$CURRENT_SCRIPT_DIRECTORY = $CURRENT_SCRIPT_DIRECTORY -or (Split-Path -Parent $MyInvocation.MyCommand.Path)
$CURRENT_SCRIPT_FILENAME = $CURRENT_SCRIPT_FILENAME -or (Split-Path -Leaf $MyInvocation.MyCommand.Path)
$CURRENT_SCRIPT_FILENAME_BASE = [System.IO.Path]::GetFileNameWithoutExtension($CURRENT_SCRIPT_FILENAME)

# Import shared functions (assuming there’s a shared_functions.ps1)
$SHARED_EXT_SCRIPTS_PATH = $SHARED_EXT_SCRIPTS_PATH -or $CURRENT_SCRIPT_DIRECTORY
. "$SHARED_EXT_SCRIPTS_PATH\SharedFunctions.ps1"

# Function to rename files and directories
function Rename-FilesAndDirectories {
    param (
        [string]$ProjectName,
        [string]$NewProjectName
    )

    # Find files and directories matching the project name and rename them
    Get-ChildItem -Recurse -Depth 99 -Filter "*$ProjectName*" | ForEach-Object {
        $newItem = $_.FullName -replace $ProjectName, $NewProjectName
        Rename-Item -Path $_.FullName -NewName $newItem
    }

    $PROJECT_NAME_UPPERCASE = $ProjectName.ToUpper()
    $NEW_PROJECT_NAME_UPPERCASE = $NewProjectName.ToUpper()

    # Rename files and directories in uppercase
    Get-ChildItem -Recurse -Depth 99 -Filter "*$PROJECT_NAME_UPPERCASE*" | ForEach-Object {
        $newItem = $_.FullName -replace $PROJECT_NAME_UPPERCASE, $NEW_PROJECT_NAME_UPPERCASE
        Rename-Item -Path $_.FullName -NewName $newItem
    }
}

# Function to replace text within files
function Replace-TextInFiles {
    param (
        [string]$ProjectName,
        [string]$NewProjectName
    )

    Write-Host "Replacing text in files from '$ProjectName' to '$NewProjectName'..."

    # Replace text within files
    Get-ChildItem -Recurse -File | ForEach-Object {
        (Get-Content $_.FullName) -replace $ProjectName, $NewProjectName | Set-Content $_.FullName
    }
}

# Check if a new project name is provided as a command-line argument
if (-not $args) {
    # Prompt the user for the new project name if no argument is given
    $new_project_name = Read-Host "Enter the new project name"
} else {
    $new_project_name = $args[0]
}

$PROJECT_NAME = "python-project-template"

# Rename files, directories, and replace text in files
Rename-FilesAndDirectories -ProjectName $PROJECT_NAME -NewProjectName $new_project_name
Replace-TextInFiles -ProjectName $PROJECT_NAME -NewProjectName $new_project_name

Write-Host "Renaming and text replacement complete!"
exit 0
