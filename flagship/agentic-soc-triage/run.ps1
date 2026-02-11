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
pip -q install -U pip | Out-Null
pip -q install pydantic | Out-Null

& $Python -m pipelines.run
