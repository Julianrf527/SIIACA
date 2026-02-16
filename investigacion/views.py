from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Investigacion, Noticia, Suscrito, Destacado, ConfiguracionSitio


def index(request):
    """
    Vista principal (home) - code (1).html
    Muestra:
    - 3 imágenes destacadas en carrusel
    - 5 investigaciones más recientes (carrusel de 2 en 2, scroll de 1 en 1)
    - 3 noticias más recientes (carrusel)
    """
    destacados = Destacado.objects.filter(activo=True)[:3]
    investigaciones_recientes = Investigacion.objects.all()[:5]
    noticias_recientes = Noticia.objects.all()[:3]
    config = ConfiguracionSitio.load()
    
    context = {
        'destacados': destacados,
        'investigaciones': investigaciones_recientes,
        'noticias': noticias_recientes,
        'config': config,
    }
    
    return render(request, 'investigacion/index.html', context)


def investigaciones_listado(request):
    """
    Vista de listado de investigaciones - code.html
    Con búsqueda y paginación
    """
    # Obtener parámetros de búsqueda
    query = request.GET.get('q', '')
    tag = request.GET.get('tag', '')
    
    # Filtrar investigaciones
    investigaciones = Investigacion.objects.all()
    
    if query:
        investigaciones = investigaciones.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(autores__icontains=query)
        )
    
    if tag:
        investigaciones = investigaciones.filter(tags=tag)
    
    # Paginación (6 por página)
    paginator = Paginator(investigaciones, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Obtener todos los tags únicos
    tags_disponibles = Investigacion.TAGS_CHOICES
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'tag_actual': tag,
        'tags_disponibles': tags_disponibles,
    }
    
    return render(request, 'investigacion/investigaciones.html', context)


def suscribirse(request):
    """
    Vista para procesar la suscripción al boletín
    """
    if request.method == 'POST':
        correo = request.POST.get('correo', '').strip()
        
        if correo:
            # Verificar si ya está suscrito
            if Suscrito.objects.filter(correo=correo).exists():
                messages.warning(request, 'Este correo ya está suscrito.')
            else:
                # Crear nueva suscripción
                Suscrito.objects.create(correo=correo)
                messages.success(request, '¡Suscripción exitosa! Recibirás nuestro boletín mensual.')
        else:
            messages.error(request, 'Por favor, ingresa un correo válido.')
    
    # Redirigir a la página de inicio
    return redirect('index')
