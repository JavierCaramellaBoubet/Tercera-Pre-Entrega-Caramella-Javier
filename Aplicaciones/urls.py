from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home),
    path('registrarCompra/', views.registrarCompra),
    path('edicionCompra/<codigo>', views.edicionCompra),
    path('editarCompra/', views.editarCompra),
    path('eliminarCompra/<codigo>', views.eliminarCompra),
    path('ruta5/', views.vista5, name='vista5'),


]