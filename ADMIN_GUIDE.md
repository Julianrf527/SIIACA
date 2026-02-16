# Guía del Panel de Administración

## 🔐 Acceso al Panel Admin

### URL de Acceso

```
http://127.0.0.1:8000/admin/
```

### Credenciales Por Defecto

```
Usuario:    admin
Contraseña: admin
Email:      julianrf527@gmail.com
```

⚠️ **IMPORTANTE**: Cambia estas credenciales en producción por seguridad.

## 🚀 Inicio Rápido

### 1. Crear el Superusuario

**Opción A: Usar credenciales por defecto**

```powershell
python manage.py crear_superusuario
```

**Opción B: Crear usuario personalizado**

```powershell
python manage.py createsuperuser
```

### 2. Restablecer Contraseña

Si olvidaste la contraseña del admin:

```powershell
python manage.py changepassword admin
```

O usa el script incluido:

```powershell
python manage.py crear_superusuario  # Restablece a admin/admin
```

## 📋 Funcionalidades del Admin

### Dashboard Principal

Al acceder verás 4 secciones principales:

1. **Investigaciones** - Gestión de proyectos e investigaciones
2. **Noticias** - Gestión de noticias del semillero
3. **Suscritos** - Lista de correos suscritos al boletín
4. **Destacados** - Imágenes del carrusel principal

## 🔬 Gestión de Investigaciones

### Campos Disponibles

- **Título**: Nombre de la investigación
- **Autores**: Nombres de los autores (ej: "García, J. et al.")
- **Categoría (Tags)**: Riego y Drenaje, Poscosecha, Tecnología, etc.
- **Descripción**: Descripción completa del proyecto
- **Foto**: Imagen representativa (Recomendado: 800x600px)
- **Documento PDF**: Archivo PDF del documento
- **Fecha de Publicación**: Fecha de la investigación

### Características

- ✅ Vista previa de fotos en miniatura
- ✅ Indicador de PDF adjunto
- ✅ Búsqueda por título, descripción o autores
- ✅ Filtros por categoría y fecha
- ✅ Ordenamiento por fecha (más recientes primero)
- ✅ 20 items por página

### Acciones en Lote

- **Marcar como Poscosecha**: Cambia la categoría a Poscosecha
- **Marcar como Tecnología**: Cambia la categoría a Tecnología

### Cómo Agregar una Investigación

1. Click en **"Investigaciones"** → **"Agregar investigación"**
2. Completa los campos requeridos
3. Sube la foto (JPG, PNG)
4. Sube el documento PDF
5. Selecciona la categoría
6. Click en **"Guardar"**

### Cómo Editar una Investigación

1. Click en **"Investigaciones"**
2. Click en la investigación que deseas editar
3. Modifica los campos necesarios
4. Click en **"Guardar"** o **"Guardar y continuar editando"**

### Cómo Eliminar una Investigación

1. Click en **"Investigaciones"**
2. Selecciona las investigaciones con checkbox
3. En el dropdown "Acción": selecciona "Eliminar investigaciones seleccionadas"
4. Click en **"Ejecutar"**
5. Confirma la eliminación

## 📰 Gestión de Noticias

### Campos Disponibles

- **Título**: Nombre de la noticia
- **Categoría**: CONGRESO 2024, ACADÉMICO, INFRAESTRUCTURA, etc.
- **Descripción**: Contenido completo de la noticia
- **Foto**: Imagen de la noticia (Recomendado: 800x600px)
- **Fecha de Publicación**: Fecha de la noticia

### Características

- ✅ Vista previa de fotos
- ✅ Vista corta de descripción (50 caracteres)
- ✅ Búsqueda por título o descripción
- ✅ Filtros por categoría y fecha
- ✅ 20 noticias por página

### Acciones en Lote

- **Marcar como Congreso**: Cambia categoría a CONGRESO 2024
- **Marcar como Académico**: Cambia categoría a ACADÉMICO

### Cómo Agregar una Noticia

1. Click en **"Noticias"** → **"Agregar noticia"**
2. Completa título, categoría y descripción
3. Sube la foto
4. Selecciona la fecha
5. Click en **"Guardar"**

## 📧 Gestión de Suscritos

### Información Disponible

- **Correo**: Email del suscrito
- **Fecha de Suscripción**: Cuándo se suscribió
- **Antigüedad**: Días desde la suscripción

### Características

- ✅ Solo lectura (los usuarios se suscriben desde el sitio)
- ✅ Búsqueda por correo
- ✅ Fecha de suscripción como fecha de solo lectura
- ✅ 50 suscritos por página

### Exportar Correos

1. Selecciona los suscritos con checkbox
2. En el dropdown "Acción": selecciona "Exportar correos seleccionados a CSV"
3. Click en **"Ejecutar"**
4. Se descargará un archivo `suscritos.csv`

Este archivo puede usarse para:

- Enviar boletines por email
- Importar a Mailchimp u otras plataformas
- Análisis de suscriptores

### Eliminar Suscritos

1. Selecciona los suscritos
2. Acción: "Eliminar suscritos seleccionados"
3. Confirmar

## 🎨 Gestión de Destacados (Carrusel)

### Campos Disponibles

- **Título**: Título del destacado
- **Descripción**: Descripción breve
- **Imagen**: Imagen para el carrusel (Recomendado: 1200x450px)
- **Orden**: Número de orden (1, 2, 3)
- **Activo**: Si está activo o no

### Características

- ✅ Vista previa de imagen (más grande)
- ✅ Edición inline del orden y estado activo
- ✅ Solo muestra 3 destacados activos en el sitio
- ✅ 10 items por página

### Acciones en Lote

- **Activar destacados**: Activa los seleccionados
- **Desactivar destacados**: Desactiva los seleccionados

### ⚠️ Regla Importante

**Solo se mostrarán 3 destacados activos en el carrusel principal del sitio.**

Si hay más de 3 activos, solo se mostrarán los primeros 3 según el orden.

### Cómo Configurar el Carrusel

1. Click en **"Destacados"** → **"Agregar destacado"**
2. Completa título y descripción
3. Sube imagen (1200x450px para mejor visualización)
4. Asigna **orden** (1 = primera posición)
5. Marca como **activo**
6. Click en **"Guardar"**

Repite para crear 3 destacados.

### Cambiar Orden Rápidamente

1. Ve a la lista de **"Destacados"**
2. Edita el número en la columna **"Orden"** directamente
3. Marca/desmarca **"Activo"** directamente
4. Los cambios se guardan automáticamente

## 🎨 Personalización Visual

El panel admin está personalizado con los colores del semillero:

- **Color Principal**: Verde neón (#13ec13)
- **Color Oscuro**: #102210
- **Botones**: Verde con texto negro
- **Header**: Gradiente verde oscuro
- **Footer**: Personalizado con email de contacto

## 🔍 Búsqueda y Filtros

### Búsqueda General

Cada sección tiene una barra de búsqueda en la parte superior derecha.

**Investigaciones**: Busca en título, descripción y autores
**Noticias**: Busca en título y descripción
**Suscritos**: Busca por correo

### Filtros Laterales

En el lado derecho verás filtros para:

**Investigaciones**:

- Por categoría (tags)
- Por fecha de publicación (año/mes/día)

**Noticias**:

- Por categoría
- Por fecha de publicación

**Suscritos**:

- Por fecha de suscripción

### Jerarquía de Fechas

En la parte superior de cada listado, puedes filtrar por:

- Año
- Mes
- Día

## 📊 Estadísticas Rápidas

En el dashboard principal verás:

- **Total de investigaciones**
- **Total de noticias**
- **Total de suscritos**
- **Total de destacados**

## 🛠️ Comandos Útiles

### Crear/Restablecer Admin

```powershell
python manage.py crear_superusuario
```

### Cambiar Contraseña

```powershell
python manage.py changepassword admin
```

### Cargar Datos de Ejemplo

```powershell
python manage.py cargar_datos_ejemplo
```

### Hacer Backup

```powershell
python manage.py dumpdata investigacion > backup.json
```

### Restaurar Backup

```powershell
python manage.py loaddata backup.json
```

## 🔒 Seguridad

### Buenas Prácticas

1. **Cambia las credenciales por defecto** en producción
2. **Usa contraseñas fuertes** (mínimo 12 caracteres)
3. **No compartas** las credenciales
4. **Haz backups** regulares de la base de datos
5. **Configura email** para recuperación de contraseña

### Configurar Email de Recuperación

En `settings.py` agrega:

```python
# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'julianrf527@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-app-password'
DEFAULT_FROM_EMAIL = 'julianrf527@gmail.com'
```

**Para Gmail**: Usa "App Passwords" en vez de tu contraseña normal.

### Recuperar Contraseña

1. En la página de login, click en **"¿Has olvidado tu contraseña?"**
2. Ingresa el email: julianrf527@gmail.com
3. Recibirás un email con el link de recuperación
4. Sigue las instrucciones para crear nueva contraseña

## 📱 Responsive

El panel admin de Django es **responsive** y funciona en:

- 💻 Desktop
- 📱 Tablets
- 📱 Móviles

## 🎓 Tips y Trucos

### 1. Edición Rápida

Para **Destacados**, puedes editar **orden** y **activo** directamente desde la lista sin entrar a cada registro.

### 2. Copiar Registros

Para duplicar una investigación o noticia:

1. Entra al registro
2. Click en **"Guardar como nuevo"** (en la esquina inferior derecha)
3. Modifica los campos necesarios

### 3. Historial de Cambios

Django guarda un historial de todos los cambios. Para verlo:

1. Entra a cualquier registro
2. Click en **"Historial"** (esquina superior derecha)
3. Verás quién y cuándo hizo cada cambio

### 4. Búsqueda Avanzada

Puedes combinar búsqueda + filtros para encontrar registros específicos:

1. Escribe en la búsqueda
2. Aplica filtros laterales
3. Los resultados se actualizan automáticamente

### 5. Atajos de Teclado

- **Alt + S**: Guardar
- **Alt + A**: Guardar y agregar otro
- **Alt + C**: Guardar y continuar editando

## ⚠️ Solución de Problemas

### No puedo acceder al admin

**Problema**: Error de credenciales

**Solución**:

```powershell
python manage.py crear_superusuario
```

### Las imágenes no se muestran

**Problema**: Archivos media no configurados

**Solución**:

1. Verifica que la carpeta `media/` exista
2. Verifica `settings.py`:

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Error al subir archivos

**Problema**: Carpetas no existen

**Solución**:

```powershell
New-Item -ItemType Directory -Force -Path media,media/investigaciones,media/noticias,media/destacados,media/documentos
```

### No aparece el botón de exportar CSV

**Problema**: No has seleccionado ningún registro

**Solución**: Marca al menos un checkbox antes de seleccionar la acción

## 📚 Recursos Adicionales

- [Documentación Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
- [Personalización del Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

## 🆘 Soporte

Para problemas o preguntas:

- **Email**: julianrf527@gmail.com
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

**¡Panel de Administración Configurado y Listo para Usar! 🚀**
