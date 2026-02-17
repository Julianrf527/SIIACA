@echo off
echo Ejecutando script de creación de BD si es necesario...
python scripts\create_db.py
if %errorlevel% neq 0 (
    echo Fallo al crear/verificar la BD
    exit /b %errorlevel%
)

echo Aplicando migraciones...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Fallo en migrate
    exit /b %errorlevel%
)

echo Iniciando servidor de desarrollo en 127.0.0.1:8000
python manage.py runserver 127.0.0.1:8000
