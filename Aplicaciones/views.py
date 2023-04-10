from django.shortcuts import render, redirect
from .models import Compra
from django.contrib import messages

#import datetime  #Para usar luego en el Día y Hora de la Compra
#import random    #Para usar luego en la generación del Número de Ticket




# Create your views here.


def home(request):
    compraListados = Compra.objects.all()
    messages.success(request, '¡Compras listadas!')
    return render(request, "GestionCompras.html", {"compra": compraListados})


def registrarCompra(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    #dia_compra=datetime.datetime.today()
    #print(f"Día y Hora de Compra: {dia_compra}")
    #ticket_numero= random.randrange(0,999999999999)

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


