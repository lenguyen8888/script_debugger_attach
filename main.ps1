# Optional: Import the module here if you want to test functions interactively
Import-Module "$PSScriptRoot\MyFunctions.psm1"

Write-Host "PowerShell main script running..."

# set PYTHON_DEBUG to 1 to enable debug messages in child.py
$env:PYTHON_DEBUG = 1
# Launch Python child script
Start-Process -FilePath "python.exe" -ArgumentList "$PSScriptRoot\child.py" -NoNewWindow -Wait
