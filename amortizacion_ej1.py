print("Ejercicio de Amortización")
deudaInicial = float(input("Ingrese el monto a prestar: "))
periodos = int(input("Digite el tiempo del crédito: "))
interes = 0.01   # Equivalente a 10%
amortizacion = deudaInicial / periodos

pago = 0
intereses = 0
totalPagado = 0
saldoActual = deudaInicial

for i in range(periodos):
    saldoActual = saldoActual + intereses - pago
    intereses = interes * saldoActual
    pago = intereses + amortizacion
    totalPagado = totalPagado + pago
    print("Periodo", i+1,"Deuda Inicial $ {0:.2f}".format(saldoActual), " La tasa es de $ {0:.2f}".format(interes), " Los intereses son $ {0:.2f}".format(intereses), " La Amortización es de $ {0:.2f}".format(amortizacion), " El pago es de $ {0:.2f}".format(pago))

print("El total pagado fue $ {0:.2f}".format(totalPagado))