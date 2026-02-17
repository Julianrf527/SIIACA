from django.shortcuts import render


def custom_404(request, exception=None):
    """Renderiza una página 404 personalizada con un icono."""
    return render(request, '404.html', status=404)


def preview_404(request):
    """Devuelve la plantilla 404 para previsualización en DEBUG sin cambiar settings."""
    return render(request, '404.html', status=404)
