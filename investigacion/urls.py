from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('investigaciones/', views.investigaciones_listado, name='investigaciones'),
    path('noticia/<int:pk>/', views.noticia_detalle, name='noticia_detalle'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
]
