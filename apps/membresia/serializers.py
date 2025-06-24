from rest_framework import serializers
from .models import *


class membresiaSerializer(serializers.ModelSerializer):
    tipo_vehiculo= models.TextField(("tipo_vehiuculo"))
    placa_vehiculo= models.TextField(("placa_vehiculo"))
    h_d_m= models.IntegerField(("h_d_m"))
    login_id=models.IntegerField(("login"))