from django.shortcuts import render
from proyectofinal.models import Operacion, CCL, Portfolio
from proyectofinal.forms import Buscar
from django.views import View
from django.views.generic import CreateView

# View operaciones

class OperacionCrear(CreateView):
  model = Operacion
  success_url = "/operaciones"
  fields = ["fecha", "cliente", "direccion", "usd", "fx_rate"]

def mostrar_operaciones(request):
  detalle_operaciones = Operacion.objects.all()
  return render(request, "proyectofinal/operaciones.html", {"detalle_operaciones": detalle_operaciones})

# View ccl

class CCLcrear(CreateView):
  model = CCL
  success_url = "/ccl"
  fields = ["empresa", "ticker", "precio_arg", "ratio", "precio_usa"]

def mostrar_ccl(request):
  detalle_ccl = CCL.objects.all()
  return render(request, "proyectofinal/ccl.html", {"detalle_ccl": detalle_ccl})

# View Portfolio Acciones

class PortfolioCrear(CreateView):
  model = Portfolio
  success_url = "/detalle-Portfolio"
  fields = ["empresa", "ticker", "media", "sdev", "weight"]


def portfolio(request):
  detalle_portfolio = Portfolio.objects.all()
  return render(request, "proyectofinal/portfolio.html", {"detalle_portfolio": detalle_portfolio})

class BuscarPortfolio(View):
    form_class = Buscar
    template_name = 'proyectofinal/portfolio-buscar.html'
    initial = {"empresa":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data.get("empresa")
            detalle_portfolio = Portfolio.objects.filter(empresa__icontains=empresa).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'detalle_portfolio':detalle_portfolio})
        return render(request, self.template_name, {"form": form})

