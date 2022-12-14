from django.db import models

# Modelo operaciones

class Operacion(models.Model):
    fecha = models.DateField()
    cliente = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    usd = models.IntegerField()
    fx_rate = models.IntegerField()

def __str__(self):
    return f"{self.id}, {self.fecha}, {self.cliente}, {self.direccion}, {self.usd}, {self.fx_rate}"

# Modelo CCL - Contado con liqui implicito

class CCL(models.Model):
    empresa = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    precio_arg = models.FloatField()
    ratio = models.IntegerField()
    precio_usa = models.FloatField()

def __str__(self):
    return f"{self.empresa}, {self.ticker}, {self.precio_arg}, {self.ratio}, {self.precio_usa}"

# Modelo Portfolio Acciones

class Portfolio(models.Model):
   empresa = models.CharField(max_length=100)
   ticker = models.CharField(max_length=10)
   media = models.FloatField()
   sdev = models.FloatField()
   weight = models.FloatField()

def __str__(self):
    return f"{self.empresa}, {self.ticker}, {self.media}, {self.sdev}, {self.weight}"