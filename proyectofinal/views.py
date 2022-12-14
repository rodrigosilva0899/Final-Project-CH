from django.shortcuts import render
from proyectofinal.models import Operacion, CCL, Portfolio
from django.views.generic import CreateView

class CCLcrear(CreateView):
  model = CCL
  success_url = "/ccl"
  fields = ["empresa", "ticker", "precio_arg", "ratio", "precio_usa"]

class OperacionCrear(CreateView):
  model = Operacion
  success_url = "/operaciones"
  fields = ["fecha", "cliente", "direccion", "usd", "fx_rate"]

class PortfolioCrear(CreateView):
  model = Portfolio
  success_url = "/detalle-Portfolio"
  fields = ["empresa", "ticker", "media", "sdev", "weight"]


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