from django.shortcuts import render
from proyectofinal.models import Operacion, Cedear, AccionUSA

# View operaciones

def mostrar_operaciones(request):
  detalle_operaciones = Operacion.objects.all()
  return render(request, "proyectofinal/operaciones.html", {"detalle_operaciones": detalle_operaciones})

# View cedear

def mostrar_cedears(request):
  detalle_cedears = Cedear.objects.all()
  return render(request, "proyectofinal/cedears.html", {"detalle_cedears": detalle_cedears})

# View accion USA

def mostrar_accion_usa(request):
  detalle_accion_usa = AccionUSA.objects.all()
  return render(request, "proyectofinal/accion-usa.html", {"detalle_accion_usa": detalle_accion_usa})