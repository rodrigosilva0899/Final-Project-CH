from proyectofinal.models import Operacion, CCL, Portfolio

Operacion(fecha="2022-01-01", cliente="Lucas", direccion="Belgrano 123", usd=1000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Juan", direccion="Pinto 123", usd=2000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Martin", direccion="San Martin 123", usd=-3000, fx_rate=153).save()

CCL(empresa="Apple", ticker="APPL.BA", precio_arg=2920.0, ratio=10, precio_usa=282.0).save()
CCL(empresa="Microsoft", ticker="MSFT.BA", precio_arg=3695.0, ratio=5, precio_usa=178.6).save()
CCL(empresa="Mercado Libre", ticker="MELI.BA", precio_arg=31600.0, ratio=2, precio_usa=597.5).save()
CCL(empresa="Google", ticker="GOOGL.BA", precio_arg=4532.0, ratio=29, precio_usa=1279.0).save()
CCL(empresa="Coca Cola", ticker="KO.BA", precio_arg=988.0, ratio=5, precio_usa=48.1).save()

Portfolio(empresa="Apple", ticker="APPL", media=0.05, sdev=0.04, weight=0.60).save()
Portfolio(empresa="Amazon", ticker="AMZN", media=0.04, sdev=0.06, weight=0.40).save()

print("Se cargo con éxito toda la información")

