from django.shortcuts import render
from proyectofinal.models import Operacion, CCL, Portfolio

# View operaciones

def mostrar_operaciones(request):
  detalle_operaciones = Operacion.objects.all()
  return render(request, "proyectofinal/operaciones.html", {"detalle_operaciones": detalle_operaciones})

# View ccl

def mostrar_ccl(request):
  detalle_ccl = CCL.objects.all()
  return render(request, "proyectofinal/ccl.html", {"detalle_ccl": detalle_ccl})

# View Portfolio Acciones

def portfolio(request):
  detalle_portfolio = Portfolio.objects.all()
  return render(request, "proyectofinal/portfolio.html", {"detalle_portfolio": detalle_portfolio})