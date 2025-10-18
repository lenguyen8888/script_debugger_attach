function Show-Trace {
    param([string]$Message)
    Write-Host "TRACE: $Message"
}

function Show-Greeting {
    Write-Host "Hello from PowerShell!"
}
