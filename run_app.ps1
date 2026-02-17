param(
    [string]$BindHost = '127.0.0.1',
    [int]$BindPort = 8000
)

Write-Host "Ejecutando script de creación de BD si es necesario..."
python .\scripts\create_db.py
if ($LASTEXITCODE -ne 0) { Write-Error "Fallo al crear/verificar la BD"; exit $LASTEXITCODE }

Write-Host "Aplicando migraciones..."
python manage.py migrate
if ($LASTEXITCODE -ne 0) { Write-Error "Fallo en migrate"; exit $LASTEXITCODE }

Write-Host "Creando superusuario por defecto (si no existe)..."
python manage.py crear_superusuario
if ($LASTEXITCODE -ne 0) { Write-Error "Fallo al crear el superusuario"; exit $LASTEXITCODE }

Write-Host "Cargando datos de ejemplo (si aplica)..."
python manage.py cargar_datos_ejemplo
if ($LASTEXITCODE -ne 0) { Write-Error "Fallo al cargar datos de ejemplo"; exit $LASTEXITCODE }

$address = "$($BindHost):$($BindPort)"
Write-Host "Iniciando servidor de desarrollo en $address"
python manage.py runserver $address
