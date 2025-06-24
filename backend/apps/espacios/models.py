from django.db import models

# Create your models here.
class espacios(models.Model):
    disponible= models.BooleanField(("disponible"))
    reservado= models.TextField(("reservado"))
    discapacitado= models.IntegerField(("discapacitados"))
    electrico= models.IntegerField(("electrico"))
    moto= models.IntegerField(("moto"))
    tarifa_id=models.IntegerField(("tarifa"))