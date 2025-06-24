from rest_framework import serializers
from .models import *


class tarifasSerializer(serializers.ModelSerializer):
    moto= models.TextField(("moto"))
    carro= models.TextField(("carro"))
    vip= models.TextField(("vip"))