from rest_framework import serializers
from .models import *


class espaciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = espacios
        fields = ('__all__')
