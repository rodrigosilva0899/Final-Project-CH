# Final-Project-CH
Final Project

El proyecto final es una aplicación que consta de 3 partes:

1) Operaciones: este es un model que tiene como objetivo ser un ABM de operaciones de FX USD/ARS.

2) CCL: este es un model que tiene como objetivo ser un ABM de acciones que cotizan en Argentina y que
completando el precio del cedear, el precio del activo en USA y el ratio de conversión entre ambas, (más adelante en la entrega final) se pueda calcular el tipo de cambio CCL implicito que surge de estos activos y su desvío con el tipo de cambio CCL Real.

    Los cedears son instrumentos (Certificados de Deposito Argentinos) que pueden ser negociados en la bolsa local, y que representan acciones de empresas que cotizan en el extranjero
    Caracteristicas y atractivos:
        - Salir del riesgo Argentino, entrar en el riesgo USA.
        - Se operan localmente en pesos.
        - Cada cedear tiene su ratio de conversion.
        - Los dividendos se cobran en USD cable.
    Los cedears ajustan el precio por 2 grandes variables:
        - Performance del subyacente (accion propiamente dicha)
        - Dólar (contado con liqui).
    De acuerdo al ratio de cada Cedear, se puede determinar cual es el tipo de cambio (CCL) implicito comparando el precio de Cedear vs. Precio de la accion propiamente dicha.

3) Portfolio: es un model que tiene como objetivo ser un ABM de la tenencia en acciones de un inversor y que (más adelante en la entrega final) se pueda calcular las caracteristicas del portfolio del inversor.



Pasos:

Model Operaciones:
Completar fecha, cliente, direccion, cantidad de USD (en negativo si es venta o positivo si es compra) y tipo de cambio.

Model CCL:
Completar Empresa, ticker, precio del CEDEAR en Argentina, ratio y precio del activo en USA.

Model Portfolio:
Completar Empresa, ticker, retorno medio, desvío estándar y peso en el portfolio.
Importante: el retorno medio y desvío estándar deben ser calculados sobre el mismo periodo de tiempo (anual, mensual, semestral, etc.)