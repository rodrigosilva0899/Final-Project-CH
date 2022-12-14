from django.shortcuts import render
from proyectofinal.models import Operacion

# Create your views here.

def mostrar_operaciones(request):
  detalle_operaciones = Operacion.objects.all()
  return render(request, "proyectofinal/operaciones.html", {"detalle_operaciones": detalle_operaciones})


