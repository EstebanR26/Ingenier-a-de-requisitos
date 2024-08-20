
def CalcularPago(MetrosCubicos, PrecioPorMetroCubico):
    return MetrosCubicos * PrecioPorMetroCubico

MetrosCubicos = float(input("Ingrese el número de metros cúbicos de agua consumidos: "))
PrecioPorMetroCubico= float(input("Ingrese el precio por metro cúbico de agua: "))

PagoTotal = CalcularPago(MetrosCubicos, PrecioPorMetroCubico)

print(f"El pago total por {MetrosCubicos} metros cúbicos de agua es: ${PagoTotal:.2f}")