from django.shortcuts import render, redirect
from .models import Compra
from django.contrib import messages

# Create your views here.


def home(request):
    compraListados = Compra.objects.all()
    messages.success(request, '¡Compras listadas!')
    return render(request, "GestionCompras.html", {"cursos": compraListados})


def registrarCompra(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    compra = Compra.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    messages.success(request,'¡Compra registrada!')
    return redirect('/')


def edicionCompra(request, codigo):
    compra = Compra.objects.get(codigo=codigo)
    return render(request, "EdicionCompra.html", {"compra": compra})


def editarCompra(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    cantidad = Compra.objects.get(codigo=codigo)
    Compra.nombre = nombre
    Compra.cantidad = cantidad
    Compra.save()

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
