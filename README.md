# Semillero Ingeniería Agrícola - UNAL

## Proyecto Django con PostgreSQL

Este es un proyecto Django para el Semillero de Ingeniería Agrícola de la Universidad Nacional de Colombia. Gestiona investigaciones, noticias, suscritos y contenido destacado.

## Tecnologías

- Python 3.8+
- Django 4.2.7
- PostgreSQL 13+
- TailwindCSS (via CDN)

## Estructura de la Base de Datos

### Tablas Principales

#### Investigaciones

- `id` (autoincrement)
- `foto` (not null) - Imagen de la investigación
- `descripcion` (not null) - Descripción completa
- `fecha_publicacion` (not null) - Fecha de publicación
- `url_doc` (not null) - Documento PDF
- `tags` - Categorías: Poscosecha, Agroindustria, Riego y Drenaje, etc.
- `titulo` - Título de la investigación
- `autores` - Autores de la investigación

#### Noticias

- `id` (autoincrement)
- `foto` (not null) - Imagen de la noticia
- `descripcion` (not null) - Descripción completa
- `fecha_publicacion` (not null) - Fecha de publicación
- `titulo` - Título de la noticia
- `categoria` - Categoría de la noticia

#### Suscritos

- `id` (autoincrement)
- `correo` - Correo electrónico (único)
- `fecha_suscripcion` - Fecha y hora de suscripción

#### Destacados

- `id` (autoincrement)
- `imagen` - Imagen destacada para el carrusel
- `titulo` - Título del destacado
- `descripcion` - Descripción
- `orden` - Orden de visualización
- `activo` - Si está activo o no

## Instalación

### 1. Clonar el repositorio o tener los archivos

```powershell
cd "C:\Users\julia\Escritorio\Semillero-Ing.Agricola-UNAL"
```

### 2. Crear y activar entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

#### Opción A: Instalar PostgreSQL localmente

1. Descargar PostgreSQL desde: https://www.postgresql.org/download/windows/
2. Instalar con el instalador (anotar la contraseña del usuario postgres)
3. Abrir pgAdmin o psql y crear la base de datos:

```sql
CREATE DATABASE semillero_db;
```

#### Opción B: Usar Docker (recomendado)

```powershell
docker run --name semillero-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=semillero_db -p 5432:5432 -d postgres:13
```

### 5. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto (copiar de `.env.example`):

```env
SECRET_KEY=tu-secret-key-super-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=semillero_db
DB_USER=postgres
DB_PASSWORD=tu-contraseña-postgres
DB_HOST=localhost
DB_PORT=5432
```

### 6. Ejecutar migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario

```powershell
python manage.py createsuperuser
```

### 8. Cargar datos de ejemplo (opcional)

```powershell
python manage.py loaddata initial_data.json
```

### 9. Crear directorios para medios

```powershell
New-Item -ItemType Directory -Force -Path media, media/investigaciones, media/noticias, media/destacados, media/documentos
```

### 10. Ejecutar el servidor

```powershell
python manage.py runserver
```

Visitar: http://127.0.0.1:8000/

## Panel de Administración

Acceder a: http://127.0.0.1:8000/admin/

Aquí podrás gestionar:

- **Investigaciones**: Agregar, editar y eliminar investigaciones con sus PDFs
- **Noticias**: Gestionar noticias del semillero
- **Suscritos**: Ver los correos suscritos al boletín
- **Destacados**: Configurar las 3 imágenes del carrusel principal

## Funcionalidades

### Página Principal (/)

- Carrusel con 3 imágenes destacadas (configurables desde admin)
- Sección de noticias recientes (3 más recientes)
- Sección de investigaciones (5 más recientes en carrusel de 2 en 2)
- Formulario de suscripción al boletín
- Información del semillero

### Página de Investigaciones (/investigaciones/)

- Búsqueda por palabra clave, título, autor
- Filtrado por categorías (tags)
- Paginación (6 investigaciones por página)
- Descarga de PDFs

### Características

- **Sin botón "Ingresar"** (eliminado según requerimientos)
- **Búsqueda funcional** que redirige a página de investigaciones
- **Carruseles**:
  - Destacados: 3 imágenes rotando automáticamente
  - Investigaciones: 2 visibles, scroll de 1 en 1
  - Noticias: 3 visibles
- **Responsive**: Funciona en móviles, tablets y desktop
- **Dark mode**: Soporte para modo oscuro

## Estructura de Archivos

```
Semillero-Ing.Agricola-UNAL/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── setup.ps1
├── start.ps1
├── semillero_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── investigacion/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
├── templates/
│   ├── base.html
│   └── investigacion/
│       ├── index.html
│       └── investigaciones.html
├── media/
│   ├── investigaciones/
│   ├── noticias/
│   ├── destacados/
│   └── documentos/
└── static/
```

> **Nota:** No existen archivos como `code.html` ni otros scripts ajenos al flujo de Django. Usa únicamente los archivos listados arriba para desarrollo y despliegue.

## Comandos Útiles

### Hacer backup de la base de datos

```powershell
python manage.py dumpdata > backup.json
```

### Restaurar backup

```powershell
python manage.py loaddata backup.json
```

### Crear migraciones

```powershell
python manage.py makemigrations
```

### Aplicar migraciones

```powershell
python manage.py migrate
```

### Ejecutar shell de Django

```powershell
python manage.py shell
```

## Solución de Problemas

### Error de conexión con PostgreSQL

1. Verificar que PostgreSQL esté corriendo:

   ```powershell
   Get-Service -Name postgresql*
   ```

2. Verificar credenciales en `.env`

3. Verificar que la base de datos exista:
   ```powershell
   psql -U postgres -l
   ```

### Error "No module named 'investigacion'"

Verificar que `investigacion` esté en `INSTALLED_APPS` en `settings.py`

### Errores de migración

```powershell
python manage.py migrate --run-syncdb
```

## Contribuir

1. Hacer fork del proyecto
2. Crear una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## Licencia

Universidad Nacional de Colombia - Semillero de Ingeniería Agrícola

## Contacto

- Email: semilleroia_bog@unal.edu.co
- Teléfono: (+57) 601 3165000
- Ubicación: Ciudad Universitaria, Bogotá
