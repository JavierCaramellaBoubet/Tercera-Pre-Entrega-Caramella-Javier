from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #path('', views.home),
    path('', views.inicio),
    path('registrarCompra/', views.registrarCompra, name="registrarCompra"),
    path('edicionCompra/<codigo>', views.edicionCompra),
    path('editarCompra/', views.editarCompra),
    path('eliminarCompra/<codigo>', views.eliminarCompra),
    
    path('', inicioApp, name="inicioApp"),
    path('contacto/', contacto, name="contacto"),
    path('promociones/', promociones, name="promociones"),

      path('crear_usuario/', views.crear_usuario, name="crear_usuario"),    

    path('buscarProducto/', buscarProducto, name="buscarProducto"),
    path('buscandoProducto/', buscandoProducto, name="buscandoProducto"),
    path('nuestraEmpresa/',views.nuestraEmpresa, name= 'nuestraEmpresa'),
    
    path('registrarEntrega/', views.registrarEntrega, name="registrarEntrega"),

   
    
]