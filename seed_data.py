from proyectofinal.models import Operacion, Cedear

Operacion(fecha="2022-01-01", cliente="Lucas", direccion="Belgrano 123", usd=1000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Juan", direccion="Pinto 123", usd=2000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Martin", direccion="San Martin 123", usd=-3000, fx_rate=153).save()

Cedear(empresa="Apple", ticker="APPL.BA", precio=2920.0, ratio=10).save()
Cedear(empresa="Microsoft", ticker="MSFT.BA", precio=3695.0, ratio=5).save()
Cedear(empresa="Mercado Libre", ticker="MELI.BA", precio=31600.0, ratio=2).save()
Cedear(empresa="Google", ticker="GOOGL.BA", precio=4532.0, ratio=29).save()
Cedear(empresa="Coca Cola", ticker="KO.BA", precio=988.0, ratio=5).save()

print("Se cargo con éxito las operaciones de prueba")

