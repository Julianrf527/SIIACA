from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('investigaciones/', views.investigaciones_listado, name='investigaciones'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
]
