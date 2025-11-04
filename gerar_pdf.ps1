# Script para gerar PDF da dissertação
# Requer Pandoc instalado: https://pandoc.org/installing.html

Write-Host "Gerando PDF da dissertação..." -ForegroundColor Green

# Lista de arquivos na ordem correta
$arquivos = @(
    "01_CAPA_E_INTRODUCAO.md",
    "02_FUNDAMENTACAO_TEORICA.md",
    "03_METODOLOGIA.md",
    "04_DESENVOLVIMENTO_SISTEMA.md",
    "05_RESULTADOS_E_DISCUSSAO.md",
    "06_CONCLUSAO_E_REFERENCIAS.md"
)

# Verificar se Pandoc está instalado
try {
    $pandocVersion = pandoc --version
    Write-Host "Pandoc encontrado!" -ForegroundColor Green
} catch {
    Write-Host "ERRO: Pandoc não está instalado!" -ForegroundColor Red
    Write-Host "Instale em: https://pandoc.org/installing.html" -ForegroundColor Yellow
    exit
}

# Verificar se todos os arquivos existem
foreach ($arquivo in $arquivos) {
    if (-not (Test-Path $arquivo)) {
        Write-Host "ERRO: Arquivo $arquivo não encontrado!" -ForegroundColor Red
        exit
    }
}

Write-Host "Todos os arquivos encontrados. Gerando PDF..." -ForegroundColor Cyan

# Gerar PDF com formatação acadêmica
pandoc $arquivos `
    -o "DISSERTACAO_APS_CALCULADORA_CARBONO.pdf" `
    --pdf-engine=xelatex `
    -V geometry:margin=3cm `
    -V geometry:top=3cm `
    -V geometry:bottom=2cm `
    -V geometry:left=3cm `
    -V geometry:right=2cm `
    -V fontsize=12pt `
    -V linestretch=1.5 `
    -V documentclass=report `
    -V lang=pt-BR `
    --toc `
    --toc-depth=3 `
    --number-sections

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nPDF gerado com sucesso!" -ForegroundColor Green
    Write-Host "Arquivo: DISSERTACAO_APS_CALCULADORA_CARBONO.pdf" -ForegroundColor Cyan
    Write-Host "`nAbrindo PDF..." -ForegroundColor Yellow
    Start-Process "DISSERTACAO_APS_CALCULADORA_CARBONO.pdf"
} else {
    Write-Host "`nERRO ao gerar PDF!" -ForegroundColor Red
    Write-Host "Verifique se o XeLaTeX está instalado (vem com MiKTeX ou TeX Live)" -ForegroundColor Yellow
}
