# Guía de Inicio Rápido - Semillero UNAL

## Configuración Rápida con PostgreSQL

### Opción 1: Instalación Automática (Recomendada)

```powershell
# Ejecutar el script de configuración
.\setup.ps1
```

Este script hará automáticamente:

- Crear entorno virtual
- Instalar dependencias
- Crear directorios necesarios
- Configurar archivos .env
- Ejecutar migraciones

### Opción 2: Instalación Manual

#### Paso 1: Configurar PostgreSQL

**Opción A: Usar Docker (Más Fácil)**

```powershell
# Instalar PostgreSQL con Docker
docker run --name semillero-postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=semillero_db `
  -p 5432:5432 `
  -d postgres:13

# Verificar que está corriendo
docker ps
```

**Opción B: Instalación Local**

1. Descargar PostgreSQL: https://www.postgresql.org/download/windows/
2. Instalar con el instalador (guardar la contraseña)
3. Abrir pgAdmin o usar psql:

```sql
-- Crear base de datos
CREATE DATABASE semillero_db;

-- Crear usuario (opcional)
CREATE USER semillero_user WITH PASSWORD 'mi_contraseña';
GRANT ALL PRIVILEGES ON DATABASE semillero_db TO semillero_user;
```

#### Paso 2: Configurar el Proyecto

```powershell
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
.\venv\Scripts\Activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear archivo .env
Copy-Item .env.example .env

# 5. Editar .env con tus credenciales
notepad .env
```

**Configuración mínima del .env:**

```env
SECRET_KEY=tu-clave-secreta-super-larga-y-aleatoria-123456789
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=semillero_db
DB_USER=postgres
DB_PASSWORD=postgres  # Tu contraseña de PostgreSQL
DB_HOST=localhost
DB_PORT=5432
```

#### Paso 3: Configurar la Base de Datos

```powershell
# 1. Crear directorios para archivos
New-Item -ItemType Directory -Force -Path media, media/investigaciones, media/noticias, media/destacados, media/documentos

# 2. Crear migraciones
python manage.py makemigrations

# 3. Aplicar migraciones
python manage.py migrate

# 4. Crear superusuario
python manage.py createsuperuser
# Usuario sugerido: admin
# Email: admin@unal.edu.co
# Contraseña: tu elección

# 5. Cargar datos de ejemplo
python manage.py cargar_datos_ejemplo
```

#### Paso 4: Ejecutar el Servidor

```powershell
python manage.py runserver
```

Abrir en el navegador:

- **Sitio principal**: http://127.0.0.1:8000/
- **Panel admin**: http://127.0.0.1:8000/admin/

## Gestión de Contenido

### 1. Panel de Administración

Acceder a: http://127.0.0.1:8000/admin/

**Credenciales**: Las que creaste con `createsuperuser`

### 2. Agregar Imágenes Destacadas (Carrusel)

1. Ir a: **Destacados** → **Agregar destacado**
2. Llenar los campos:
   - **Imagen**: Subir imagen (recomendado: 1200x450px)
   - **Título**: Título del destacado
   - **Descripción**: Descripción breve
   - **Orden**: 1, 2 o 3 (orden de aparición)
   - **Activo**: ✓ Marcar
3. Guardar

**Nota**: Solo se mostrarán 3 destacados activos en el carrusel

### 3. Agregar Investigaciones

1. Ir a: **Investigaciones** → **Agregar investigación**
2. Llenar los campos:
   - **Foto**: Imagen de la investigación (recomendado: 800x600px)
   - **Título**: Título de la investigación
   - **Autores**: Nombres de autores
   - **Descripción**: Descripción completa
   - **Fecha de publicación**: Fecha
   - **URL doc**: Subir PDF del documento
   - **Categoría**: Seleccionar (Poscosecha, Riego y Drenaje, etc.)
3. Guardar

### 4. Agregar Noticias

1. Ir a: **Noticias** → **Agregar noticia**
2. Llenar los campos:
   - **Foto**: Imagen de la noticia (recomendado: 800x600px)
   - **Título**: Título de la noticia
   - **Categoría**: Tipo de noticia (CONGRESO, ACADÉMICO, etc.)
   - **Descripción**: Descripción completa
   - **Fecha de publicación**: Fecha
3. Guardar

### 5. Gestionar Suscritos

1. Ir a: **Suscritos** → **Suscritos**
2. Ver lista de correos suscritos
3. Exportar para enviar boletines

## Verificación

### Comprobar que todo funciona:

1. **Página Principal** (http://127.0.0.1:8000/):
   - ✓ Carrusel de 3 imágenes destacadas
   - ✓ Sección de 3 noticias
   - ✓ Sección de investigaciones (5 recientes)
   - ✓ Formulario de suscripción
   - ✓ NO hay botón "Ingresar"

2. **Búsqueda**:
   - ✓ Buscar una palabra en el header
   - ✓ Debe redirigir a /investigaciones/
   - ✓ Debe mostrar resultados filtrados

3. **Investigaciones** (http://127.0.0.1:8000/investigaciones/):
   - ✓ Listado en grid de 3 columnas
   - ✓ Filtros por categoría funcionando
   - ✓ Paginación (6 por página)
   - ✓ Botones de descarga de PDF

4. **Admin**:
   - ✓ Puede agregar/editar contenido
   - ✓ Puede subir imágenes y PDFs

## Solución de Problemas Comunes

### Error: "relation does not exist"

```powershell
# Ejecutar migraciones nuevamente
python manage.py migrate
```

### Error: "connection refused" (PostgreSQL)

```powershell
# Verificar que PostgreSQL está corriendo
# Con Docker:
docker ps
docker start semillero-postgres

# Con instalación local:
Get-Service -Name postgresql*
Start-Service postgresql-x64-13
```

### Error: "FATAL: password authentication failed"

Verificar credenciales en `.env`:

- DB_USER
- DB_PASSWORD
- DB_NAME

### No se muestran imágenes

1. Verificar que el directorio `media/` existe
2. Verificar que las imágenes se subieron correctamente en admin
3. En desarrollo, Django sirve automáticamente los archivos media

### La búsqueda no funciona

Verificar que:

1. El formulario en `base.html` apunta a `{% url 'investigaciones' %}`
2. La vista `investigaciones_listado` procesa el parámetro `q`

## Comandos Útiles

```powershell
# Ver logs en tiempo real
python manage.py runserver

# Crear backup de la BD
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json

# Limpiar caché de Python
Remove-Item -Recurse -Force **\__pycache__

# Recargar datos de ejemplo
python manage.py cargar_datos_ejemplo

# Crear nueva migración
python manage.py makemigrations

# Ver SQL de migraciones
python manage.py sqlmigrate investigacion 0001

# Shell interactivo de Django
python manage.py shell
```

## Próximos Pasos

1. **Personalizar colores**: Editar en las plantillas HTML (ya están con tema verde)
2. **Agregar contenido real**: Usar el panel admin
3. **Configurar email**: Para enviar boletines a suscritos
4. **Deploy**: Configurar para producción (Heroku, Railway, etc.)

## Estructura del Proyecto

```
Semillero-Ing.Agricola-UNAL/
├── manage.py                    # Comando principal de Django
├── requirements.txt             # Dependencias
├── .env                         # Configuración (no subir a Git)
├── README.md                    # Documentación completa
├── QUICK_START.md              # Esta guía
├── setup.ps1                   # Script de configuración
│
├── semillero_project/          # Configuración del proyecto
│   ├── settings.py             # Configuración principal
│   ├── urls.py                 # URLs principales
│   └── wsgi.py                 # WSGI para deploy
│
├── investigacion/              # App principal
│   ├── models.py               # Modelos de BD
│   ├── views.py                # Lógica de vistas
│   ├── urls.py                 # URLs de la app
│   ├── admin.py                # Configuración del admin
│   └── management/             # Comandos personalizados
│       └── commands/
│           └── cargar_datos_ejemplo.py
│
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   └── investigacion/
│       ├── index.html         # Página principal
│       └── investigaciones.html # Listado
│
└── media/                     # Archivos subidos
    ├── investigaciones/       # Fotos de investigaciones
    ├── noticias/             # Fotos de noticias
    ├── destacados/           # Imágenes del carrusel
    └── documentos/           # PDFs
```

## Contacto y Soporte

Para dudas o problemas:

- Email: semilleroia_bog@unal.edu.co
- Revisar la documentación completa en README.md

---

**¡Listo para empezar a trabajar! 🚀**
