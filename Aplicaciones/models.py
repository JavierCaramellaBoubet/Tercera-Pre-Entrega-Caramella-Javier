from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Compra(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)  #Debo inluir el random para generar el código de manera aleatoria.
    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField() #Cantidad de Productos a comprar.

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.cantidad)
    


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)  
    apellido = models.CharField(max_length=50) 
    #dni =  models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        texto = "{0} ({1}) ({2})"
        return texto.format(self.nombre, self.apellido, self.email)
    

class Entrega(models.Model):
    ciudad = models.CharField(max_length=50)  #Debo inluir el random para generar el código de manera aleatoria.
    direccion = models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    hora= models.TimeField()
    comentarios = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1}) ({2}) ({3}) ({4}) ({5}) "
        return texto.format(self.ciudad,self.direccion,self.fecha_entrega,self.hora,self.comentarios)    
    

    

    
