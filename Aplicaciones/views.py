from django.shortcuts import render, redirect
from .models import Compra, Usuario, Entrega
from django.contrib import messages
from django.http import HttpResponse
from .forms import UsuarioForm
from django.shortcuts import render
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#import datetime  #Para usar luego en el Día y Hora de la Compra
#import random    #Para usar luego en la generación del Número de Ticket




# Create your views here.

def crear_usuario(request):
    if request.method=="POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario=Usuario(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            usuario.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario{usuario.nombre} creado correctamente"})
        else:
            return render(request, "crear_usuario.html", {"form": form, "mensaje":"Error al crear el estudiante"})

    else:
        form= UsuarioForm()
    return render(request, "crear_usuario.html", {"form": form}) 



    #nombre_usuario = "Javier"
    #apellido_usuario = "Caramella Boubet"
    #dni_usuario= "29725148"
    #email_usuario= "javier@caramella.com"

    #usuario= Usuario(nombre=nombre_usuario,apellido=apellido_usuario,dni=dni_usuario,email=email_usuario)
    #usuario.save()
    #respuesta=f"Usuario Creado---{nombre_usuario} - {apellido_usuario} - {dni_usuario} - {email_usuario}"

    #return HttpResponse(respuesta)

##def inicio(request):
##   return HttpResponse("BIENVENIDOS A LA PAGINA PRINCIPAL DE COMPRAS ONLINE")

def inicioApp(request):
    #return render(request, 'Aplicaciones/inicioApp.html')
    return HttpResponse("BIENVENIDOS A LA PAGINA PRINCIPAL DE LA APLICACIONES E-COMMERCE!!!")


def contacto(request):
    return render(request, 'contacto.html')       
      



def promociones(request):
    return render(request, 'promociones.html')
    #return HttpResponse("ESTAS SON LAS PROMOCIONES")

def inicio(request):
#def home(request):
    compraListados = Compra.objects.all()
    messages.success(request, '¡Compras listadas!')
    return render(request, "GestionCompras.html", {"compra": compraListados})

#########################################################################################

def registrarCompra(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']


    compra = Compra.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    messages.success(request,'¡Compra registrada!')
    return redirect('/')


def edicionCompra(request, codigo):
    compra = Compra.objects.get(codigo=codigo)
    return render(request, "edicionCompra.html", {"compra": compra})


def editarCompra(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    compra = Compra.objects.get(codigo=codigo)
    compra.nombre = nombre
    compra.cantidad = cantidad
    compra.save()

    messages.success(request, '¡Compra actualizada!')

    return redirect('/')


def eliminarCompra(request, codigo):
    compra = Compra.objects.get(codigo=codigo)
    compra.delete()

    messages.success(request, '¡Compra eliminada!')

    return redirect('/')

#####################################################################################




def registrarUsuario(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['numEmail']


    usuario = Usuario.objects.create(nombre=nombre, apellido=apellido, email=email)
    messages.success(request,'¡USUARIO REGISTRADO CORRECTAMENTE!!!')
    return redirect('/')


def edicionUsuario(request, apellido):
    usuario = Usuario.objects.get(apellido=apellido)
    return render(request, "edicionUsuario.html", {"usuario": usuario})


def editarUsuario(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['numEmail']

    usuario = Usuario.objects.get(apellido=apellido)
    usuario.nombre= nombre
    usuario.apellido= apellido
    usuario.email=email
    usuario.save()

    messages.success(request, '¡USUARIO ACTUALIZADO!')

    return redirect('/')


def eliminarUsuario(request, apellido):
    usuario = Usuario.objects.get(apellido=apellido)
    usuario.delete()

    messages.success(request, '¡USUARIO ELIMINADO!!!')

    return redirect('/')

#######################################################################################################


def buscarProducto(request):
    return render(request, 'busquedaProducto.html')

 


def buscandoProducto(request):
    productoIngresado= request.GET["nombre"]
    if productoIngresado!="":
        productos=Compra.objects.filter(nombre__icontains=productoIngresado)
        print(productos)
        return render(request, "resultadoBusquedaProducto.html", {"nombre": productos})
    else:
        return render(request, "busquedaProducto.html", {"mensaje": "POR FAVOR INGRESA UN PRODUCTO PARA BUSCAR!!!"})
    

        

def nuestraEmpresa(request):
    return render(request, 'nuestraEmpresa.html')


############################################################################################################

def registrarEntrega(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']


    entrega = Entrega.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    messages.success(request,'¡Entrega registrada!')
    return redirect('/')


def edicionEntrega(request, codigo):
    entrega = Entrega.objects.get(codigo=codigo)
    return render(request, "edicionEntrega.html", {"entrega": entrega})


def editarEntrega(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    entrega = Entrega.objects.get(codigo=codigo)
    entrega.nombre = nombre
    entrega.cantidad = cantidad
    entrega.save()

    messages.success(request, '¡Entrega actualizada!')

    return redirect('/')


def eliminarEntrega(request, codigo):
    entrega = Entrega.objects.get(codigo=codigo)
    entrega.delete()

    messages.success(request, '¡Entrega eliminada!')

    return redirect('/')