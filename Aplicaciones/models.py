from django.db import models
from django.contrib.auth.models import User

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
    email = models.EmailField() # unique LO USAMOS PARA NO REPETIR LOS DATOS DEL USUARIO, PARA QUE SEA CARGADO UNA SOLA VEZ 

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    

    
