from django.shortcuts import render, redirect
from .models import Compra, Usuario
from django.contrib import messages
from django.http import HttpResponse

#import datetime  #Para usar luego en el Día y Hora de la Compra
#import random    #Para usar luego en la generación del Número de Ticket




# Create your views here.

def crear_usuario(request):
    nombre_usuario = "Javier"
    apellido_usuario = "Caramella Boubet"
    dni_usuario= "29725148"
    email_usuario= "javier@caramella.com"

    usuario= Usuario(nombre=nombre_usuario,apellido=apellido_usuario,dni=dni_usuario,email=email_usuario)
    usuario.save()
    respuesta=f"Usuario Creado---{nombre_usuario} - {apellido_usuario} - {dni_usuario} - {email_usuario}"

    return HttpResponse(respuesta)

def inicio(request):
    return HttpResponse("BIENVENIDOS A LA PAGINA PRINCIPAL DE COMPRAS ONLINE")

def inicioApp(request):
    return render(request, 'Aplicaciones/inicioApp.html')
    #return HttpResponse("BIENVENIDOS A LA PAGINA PRINCIPAL DE LA APLICACIONES E-COMMERCE!!!")


def contacto(request):
#        contacto1= "                    ESTAMOS PARA AYUDARTE!           "
#        contacto2= "Atención al Cliente (0800-444-8484) Disponible de Lun a Vie de 9 a 18hs."
#        contacto3= "clientes@superonline.com.ar"
#        contacto4= "         AGUARDE Y SERÁ ATENDIDO POR UN REPRESENTANTE            "

#        contacto5= "###############################################################################"
#        contacto6= "-------------------------------------------------------------------------------"

#       dato_contacto= contacto1 + contacto2 + \n {contacto3} + \n {contacto4} + \n {contacto5} + \n {contacto6}
#       return render(dato_contacto)
        return HttpResponse(f"ESTOS SON LOS MEDIOS DE CONTACTO" + "\n                    ESTAMOS PARA AYUDARTE!           ")

def promociones(request):
    return render(request, 'promociones.html')
    #return HttpResponse("ESTAS SON LAS PROMOCIONES")


def home(request):
    compraListados = Compra.objects.all()
    messages.success(request, '¡Compras listadas!')
    return render(request, "GestionCompras.html", {"compra": compraListados})


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

def vista5(request):
    diccionario={}
    return render(request, "Aplicaciones/templates/base.html", context=diccionario)


