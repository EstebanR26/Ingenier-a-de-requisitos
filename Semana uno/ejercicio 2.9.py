class ejemplo3:

    def calcular_sueldo_semanal(horas_trabajadas, pago_por_hora):
        sueldo_semanal = horas_trabajadas * pago_por_hora
        return sueldo_semanal
    
print(f"El sueldo semanal del trabajador es ${sueldo_semanal:.2f}")