# Diretório do projeto baseado na localização deste script
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$DeployDir = $PSScriptRoot

# Configuração de portas
$AppPort = 8000
$CaddyPort = 8000

# Obtém o primeiro IPv4 válido da máquina
$HostIP = (
    Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {
        $_.IPAddress -notlike "127.*" -and
        $_.IPAddress -notlike "169.254.*" -and
        $_.PrefixOrigin -ne "WellKnown"
    } |
    Select-Object -First 1
).IPAddress

Write-Host "=== Iniciando Aplicativo ===" -ForegroundColor Cyan

Write-Host "Projeto    : $ProjectRoot"
Write-Host "Deploy     : $DeployDir"
Write-Host "IP do host : $HostIP"
Write-Host "Porta App  : $AppPort"
Write-Host "Porta Caddy: $CaddyPort"
Write-Host ""

# Vai para o projeto
Set-Location $ProjectRoot

# Valida Caddyfile
Write-Host "Validando Caddyfile..."

caddy validate --config "$DeployDir\Caddyfile"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Erro no Caddyfile!" -ForegroundColor Red
    exit 1
}

# Inicia Django/Waitress
Write-Host "Iniciando Django/Waitress..."

Start-Process `
    -FilePath "uv" `
    -ArgumentList "run waitress-serve --listen=127.0.0.1:$AppPort _config.wsgi:application" `
    -WorkingDirectory $ProjectRoot

Start-Sleep -Seconds 2

# Inicia Caddy
Write-Host "Iniciando Caddy..."

Start-Process `
    -FilePath "caddy" `
    -ArgumentList "run --config `"$DeployDir\Caddyfile`"" `
    -WorkingDirectory $DeployDir

Write-Host ""
Write-Host "=== Serviços iniciados ===" -ForegroundColor Green
Write-Host "Django: http://127.0.0.1:$AppPort"
Write-Host "Caddy : http://${HostIP}:$CaddyPort" -ForegroundColor Yellow
Write-Host ""
Write-Host "Acesse a aplicação através de:" -ForegroundColor Cyan
Write-Host "http://${HostIP}:$CaddyPort" -ForegroundColor Green
