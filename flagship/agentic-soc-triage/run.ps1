param(
  [string]$Python = "py"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (-not (Test-Path ".\.venv")) {
  & $Python -m venv .venv
}

& .\.venv\Scripts\Activate.ps1 | Out-Null

# Silence pip upgrade notices in demo runs
$env:PIP_DISABLE_PIP_VERSION_CHECK = "1"
$env:PIP_NO_PYTHON_VERSION_WARNING = "1"

# Install deps quietly
& $Python -m pip -q install pydantic | Out-Null

& $Python -m pipelines.run
