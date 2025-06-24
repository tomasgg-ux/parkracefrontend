from django.db import models

# Create your models here.
class entrada (models.Model):
    tipo_vehiculo= models.TextField(("tipo_vehiuculo"))
    placa_vehiculo= models.TextField(("placa_vehiculo"))
    h_d_m= models.IntegerField(("h_d_m"))
    login_id=models.IntegerField(("login"))
    