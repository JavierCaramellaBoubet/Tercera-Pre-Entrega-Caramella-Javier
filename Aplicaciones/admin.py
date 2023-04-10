from django.contrib import admin
from .models import Compra

import datetime  #Para usar luego en el Día y Hora de la Compra
import random    #Para usar luego en la generación del Número de Ticket


dia_compra=datetime.datetime.today()
#print(f"Día y Hora de Compra: {dia_compra}")
ticket_numero= random.randrange(0,999999999999)


# Register your models here.

admin.site.register(Compra)

#from .models import Compra, Inicio, Usuario, Carrito, Contacto, Promociones

#admin.site.register(Inicio)
#admin.site.register(Usuario)
#admin.site.register(Carrito)
#admin.site.register(Contacto)
#admin.site.register(Promociones)


