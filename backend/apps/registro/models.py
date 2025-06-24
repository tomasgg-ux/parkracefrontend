from django.db import models

# Create your models here.
class registro (models.Model):
    correo= models.TextField(("correo"))
    contraseña= models.TextField(("contraseña"))
    