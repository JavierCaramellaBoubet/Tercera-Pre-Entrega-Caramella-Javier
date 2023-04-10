from django.db import models

# Create your models here.

class Compra(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.cantidad)
    


#class Usuario(models.Model):
#    nombre = models.CharField(max_length=50)  
#    apellido = models.CharField(max_length=50) 
    #dni =  models.IntegerField()
#    email = models.EmailField() # unique LO USAMOS PARA NO REPETIR LOS DATOS DEL USUARIO, PARA QUE SEA CARGADO UNA SOLA VEZ 
#    dni = models.CharField(max_length=50)

#    def __str__(self):
#        return f"{self.nombre} {self.apellido} {self.email} {self.dni}"
    
#class Inicio(models.Model):
#    saludo = "Bienvenido a COMPRA ONLINE"

#    def __str__(self):
#        return f"{saludo}"
    
#class Promociones(models.Model):
#    promo= "ESTAS SON LAS PROMOCIONES"

#    def __str__(self):
#        return f"{promo}"   

#class Carrito(models.Model):
#    carrito= "ESTAS SON LOS PRODUCTOS DEL CARRITO"

#    def __str__(self):
#        return f"{carrito}"     

#class Contacto(models.Model):
#    contacto= "ESTAS SON LOS CONTACTOS"

#    def __str__(self):
#        return f"{contacto}"       
    










