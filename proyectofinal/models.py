from django.db import models

# Create your models here.

class Operacion(models.Model):
    fecha = models.DateField()
    cliente = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    usd = models.IntegerField()
    fx_rate = models.IntegerField()

def __str__(self):
    return f"{self.id}, {self.fecha}, {self.cliente}, {self.direccion}, {self.usd}, {self.fx_rate}"

class Cedear(models.Model):
    empresa = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    precio = models.FloatField()
    ratio = models.IntegerField()

def __str__(self):
    return f"{self.ticker}, {self.precio}, {self.ratio}"