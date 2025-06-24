from django.db import models

# Create your models here.
class login (models.Model):
    correo= models.TextField(("correo"))
    contraseña= models.TextField(("contraseña"))
    
    
   