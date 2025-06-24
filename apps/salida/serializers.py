from rest_framework import serializers
from .models import *


class salidaSerializer(serializers.ModelSerializer):
    ticket= models.TextField(("ticket"))
    entrada_id=models.IntegerField(("entrada"))