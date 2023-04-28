from django import forms
#from django.contrib.auth.form import UserCreationForm
from django.contrib.auth.models import User



# Create your models here.

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, label = "Nombre del Usuario")
    #nombre = forms.CharField(max_length=50, label = "Nombre del Usuario", help_text="INGRESE EL NOMBRE DEL USUARIO")
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()


   
 
    


    




