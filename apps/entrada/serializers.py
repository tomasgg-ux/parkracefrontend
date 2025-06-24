from rest_framework import serializers
from .models import *


class Entradaerializer(serializers.ModelSerializer):

    class Meta:
        model = entrada
        fields = ('__all__')