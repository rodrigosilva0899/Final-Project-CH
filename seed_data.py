from proyectofinal.models import Operacion, Cedear, AccionUSA, Portfolio

Operacion(fecha="2022-01-01", cliente="Lucas", direccion="Belgrano 123", usd=1000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Juan", direccion="Pinto 123", usd=2000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Martin", direccion="San Martin 123", usd=-3000, fx_rate=153).save()

Cedear(empresa="Apple", ticker="APPL.BA", precio=2920.0, ratio=10).save()
Cedear(empresa="Microsoft", ticker="MSFT.BA", precio=3695.0, ratio=5).save()
Cedear(empresa="Mercado Libre", ticker="MELI.BA", precio=31600.0, ratio=2).save()
Cedear(empresa="Google", ticker="GOOGL.BA", precio=4532.0, ratio=29).save()
Cedear(empresa="Coca Cola", ticker="KO.BA", precio=988.0, ratio=5).save()

AccionUSA(empresa="Apple", ticker="APPL.BA", precio=282.8).save()
AccionUSA(empresa="Microsoft", ticker="MSFT.BA", precio=178.6).save()
AccionUSA(empresa="Mercado Libre", ticker="MELI.BA", precio=597.5).save()
AccionUSA(empresa="Google", ticker="GOOGL.BA", precio=1279.0).save()
AccionUSA(empresa="Coca Cola", ticker="KO.BA", precio=48.1).save()

Portfolio(empresa="Apple", ticker="APPL", media=0.05, sdev=0.04, weight=0.60).save()
Portfolio(empresa="Amazon", ticker="AMZN", media=0.04, sdev=0.06, weight=0.40).save()

print("Se cargo con éxito toda la información")

