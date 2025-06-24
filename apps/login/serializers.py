from rest_framework import serializers
from .models import *


class loginSerializer(serializers.ModelSerializer):

    class Meta:
        model = login
        fields = ('__all__')