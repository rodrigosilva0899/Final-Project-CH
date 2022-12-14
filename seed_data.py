from proyectofinal.models import Operacion
Operacion(fecha="2022-01-01", cliente="Lucas", direccion="Belgrano 123", usd=1000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Juan", direccion="Pinto 123", usd=2000, fx_rate=150).save()
Operacion(fecha="2022-01-01", cliente="Martin", direccion="San Martin 123", usd=-3000, fx_rate=153).save()
print("Se cargo con éxito las operaciones de prueba")