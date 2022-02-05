param([Parameter(HelpMessage = "The name of the virtual environment")][string]$VirtualEnvironmentName = "")

Write-Host "Creating virtual environment"
$VirtualEnvironmentProcess = Start-Process -FilePath python -ArgumentList "-m", "venv", "./venv" -Wait

if ($null -eq $VirtualEnvironmentProcess) {
    Write-Error "Failed to start the process" -ErrorAction Stop
}