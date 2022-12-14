from django.shortcuts import render
from proyectofinal.models import Operacion, Cedear

# Create your views here.

def mostrar_operaciones(request):
  detalle_operaciones = Operacion.objects.all()
  return render(request, "proyectofinal/operaciones.html", {"detalle_operaciones": detalle_operaciones})

def mostrar_cedears(request):
  detalle_cedears = Cedear.objects.all()
  return render(request, "proyectofinal/cedears.html", {"detalle_cedears": detalle_cedears})

