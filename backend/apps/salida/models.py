from django.db import models

# Create your models here.
class salida (models.Model):
    ticket= models.TextField(("ticket"))
    entrada_id=models.IntegerField(("entrada"))
    