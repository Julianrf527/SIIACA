from django.db import models
from django.utils import timezone


class Investigacion(models.Model):
    """
    Modelo para las investigaciones del semillero
    """
    TAGS_CHOICES = [
        ('Riego y Drenaje', 'Riego y Drenaje'),
        ('Maquinaria Agrícola', 'Maquinaria Agrícola'),
        ('Poscosecha', 'Poscosecha'),
        ('Agroindustria', 'Agroindustria'),
        ('Tecnología', 'Tecnología'),
        ('Mecanización', 'Mecanización'),
        ('Hídrica', 'Hídrica'),
    ]
    
    foto = models.ImageField(upload_to='investigaciones/', verbose_name='Fotografía')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_publicacion = models.DateField(verbose_name='Fecha de Publicación', default=timezone.now)
    url_doc = models.FileField(upload_to='documentos/', verbose_name='Documento PDF')
    tags = models.CharField(max_length=50, choices=TAGS_CHOICES, verbose_name='Categoría')
    titulo = models.CharField(max_length=200, verbose_name='Título', default='')
    autores = models.CharField(max_length=200, verbose_name='Autores', default='')
    
    class Meta:
        verbose_name = 'Investigación'
        verbose_name_plural = 'Investigaciones'
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    """
    Modelo para las noticias del semillero
    """
    foto = models.ImageField(upload_to='noticias/', verbose_name='Fotografía')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_publicacion = models.DateField(verbose_name='Fecha de Publicación', default=timezone.now)
    titulo = models.CharField(max_length=200, verbose_name='Título', default='')
    categoria = models.CharField(max_length=50, verbose_name='Categoría', default='NOTICIA')
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo


class Suscrito(models.Model):
    """
    Modelo para los suscriptores del boletín
    """
    correo = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    fecha_suscripcion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Suscripción')
    
    class Meta:
        verbose_name = 'Suscrito'
        verbose_name_plural = 'Suscritos'
        ordering = ['-fecha_suscripcion']
    
    def __str__(self):
        return self.correo


class Destacado(models.Model):
    """
    Modelo para las imágenes destacadas del carrusel principal
    """
    imagen = models.ImageField(upload_to='destacados/', verbose_name='Imagen')
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción', blank=True)
    orden = models.IntegerField(default=0, verbose_name='Orden')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    
    class Meta:
        verbose_name = 'Destacado'
        verbose_name_plural = 'Destacados'
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.titulo} - Orden {self.orden}"


class ConfiguracionSitio(models.Model):
    """
    Modelo para la configuración general del sitio (Singleton)
    Solo debe existir un registro de este modelo
    """
    cantidad_proyectos = models.IntegerField(
        default=15,
        verbose_name='Cantidad de Proyectos',
        help_text='Número de proyectos completados'
    )
    cantidad_miembros = models.IntegerField(
        default=40,
        verbose_name='Cantidad de Miembros',
        help_text='Número de miembros del semillero'
    )
    cantidad_publicaciones = models.IntegerField(
        default=8,
        verbose_name='Cantidad de Publicaciones',
        help_text='Número de publicaciones científicas'
    )
    
    class Meta:
        verbose_name = 'Configuración del Sitio'
        verbose_name_plural = 'Configuración del Sitio'
    
    def save(self, *args, **kwargs):
        # Asegurar que solo existe un registro (Singleton)
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # No permitir eliminar el único registro
        pass
    
    @classmethod
    def load(cls):
        """Obtener o crear la única instancia de configuración"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return "Configuración del Sitio"
