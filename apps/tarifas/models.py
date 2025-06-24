from django.db import models

# Create your models here.
class tarifas (models.Model):
    moto= models.TextField(("moto"))
    carro= models.TextField(("carro"))
    vip= models.TextField(("vip"))

    