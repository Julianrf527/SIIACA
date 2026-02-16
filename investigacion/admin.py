from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Investigacion, Noticia, Suscrito, Destacado, ConfiguracionSitio


# Personalización del admin site
admin.site.site_header = "Semillero Ingeniería Agrícola - UNAL"
admin.site.site_title = "Admin Semillero"
admin.site.index_title = "Panel de Administración"


@admin.register(Investigacion)
class InvestigacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'tags', 'fecha_publicacion', 'preview_foto', 'tiene_documento')
    list_filter = ('tags', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion', 'autores')
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    list_per_page = 20
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'autores', 'tags')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'foto', 'url_doc')
        }),
        ('Fecha', {
            'fields': ('fecha_publicacion',)
        }),
    )
    
    def preview_foto(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.foto.url
            )
        return "Sin foto"
    preview_foto.short_description = 'Foto'
    
    def tiene_documento(self, obj):
        if obj.url_doc:
            return format_html(
                '<span style="color: green;">✓ PDF</span>'
            )
        return format_html('<span style="color: red;">✗</span>')
    tiene_documento.short_description = 'Documento'
    
    actions = ['marcar_poscosecha', 'marcar_tecnologia']
    
    def marcar_poscosecha(self, request, queryset):
        queryset.update(tags='Poscosecha')
        self.message_user(request, f'{queryset.count()} investigaciones marcadas como Poscosecha')
    marcar_poscosecha.short_description = 'Marcar como Poscosecha'
    
    def marcar_tecnologia(self, request, queryset):
        queryset.update(tags='Tecnología')
        self.message_user(request, f'{queryset.count()} investigaciones marcadas como Tecnología')
    marcar_tecnologia.short_description = 'Marcar como Tecnología'


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'preview_foto', 'descripcion_corta')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    list_per_page = 20
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'categoria')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'foto')
        }),
        ('Fecha', {
            'fields': ('fecha_publicacion',)
        }),
    )
    
    def preview_foto(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.foto.url
            )
        return "Sin foto"
    preview_foto.short_description = 'Foto'
    
    def descripcion_corta(self, obj):
        if len(obj.descripcion) > 50:
            return obj.descripcion[:50] + '...'
        return obj.descripcion
    descripcion_corta.short_description = 'Descripción'
    
    actions = ['marcar_congreso', 'marcar_academico']
    
    def marcar_congreso(self, request, queryset):
        queryset.update(categoria='CONGRESO 2024')
        self.message_user(request, f'{queryset.count()} noticias marcadas como Congreso')
    marcar_congreso.short_description = 'Marcar como Congreso'
    
    def marcar_academico(self, request, queryset):
        queryset.update(categoria='ACADÉMICO')
        self.message_user(request, f'{queryset.count()} noticias marcadas como Académico')
    marcar_academico.short_description = 'Marcar como Académico'


@admin.register(Suscrito)
class SuscritoAdmin(admin.ModelAdmin):
    list_display = ('correo', 'fecha_suscripcion', 'dias_suscrito')
    search_fields = ('correo',)
    date_hierarchy = 'fecha_suscripcion'
    ordering = ('-fecha_suscripcion',)
    list_per_page = 50
    readonly_fields = ('fecha_suscripcion',)
    
    def dias_suscrito(self, obj):
        from django.utils import timezone
        dias = (timezone.now() - obj.fecha_suscripcion).days
        return f"{dias} días"
    dias_suscrito.short_description = 'Antigüedad'
    
    actions = ['exportar_correos']
    
    def exportar_correos(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="suscritos.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Correo', 'Fecha de Suscripción'])
        
        for suscrito in queryset:
            writer.writerow([suscrito.correo, suscrito.fecha_suscripcion])
        
        return response
    exportar_correos.short_description = 'Exportar correos seleccionados a CSV'


@admin.register(Destacado)
class DestacadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'preview_imagen')
    list_filter = ('activo',)
    search_fields = ('titulo', 'descripcion')
    ordering = ('orden',)
    list_editable = ('orden', 'activo')
    list_per_page = 10
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'descripcion', 'imagen')
        }),
        ('Configuración', {
            'fields': ('orden', 'activo'),
            'description': 'Solo se mostrarán 3 destacados activos en el carrusel principal'
        }),
    )
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 100px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = 'Vista Previa'
    
    actions = ['activar', 'desactivar']
    
    def activar(self, request, queryset):
        queryset.update(activo=True)
        self.message_user(request, f'{queryset.count()} destacados activados')
    activar.short_description = 'Activar destacados'
    
    def desactivar(self, request, queryset):
        queryset.update(activo=False)
        self.message_user(request, f'{queryset.count()} destacados desactivados')
    desactivar.short_description = 'Desactivar destacados'


@admin.register(ConfiguracionSitio)
class ConfiguracionSitioAdmin(admin.ModelAdmin):
    """
    Admin para ConfiguracionSitio (Singleton)
    Solo permite editar el único registro, no se puede eliminar ni agregar más
    """
    list_display = ('__str__', 'cantidad_proyectos', 'cantidad_miembros', 'cantidad_publicaciones')
    
    fieldsets = (
        ('Estadísticas del Sitio', {
            'fields': ('cantidad_proyectos', 'cantidad_miembros', 'cantidad_publicaciones'),
            'description': 'Edita los números que se muestran en la página principal'
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permite un registro (Singleton)
        return not ConfiguracionSitio.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No se puede eliminar el único registro
        return False
