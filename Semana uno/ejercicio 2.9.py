SalarioMensual = float(input('ingresa el salario mensual:'))
HorasTrabajadasMensuales = float(input('ingrese las horas trabajadas mensualmente:'))
HorasTrabajadasSemanales = float(input('ingrese las horas trabajadas semanalmente:'))

PagoPorHora = SalarioMensual / HorasTrabajadasMensuales
PagoSemanal = HorasTrabajadasSemanales * PagoPorHora
print('tu salario por hora es de', PagoPorHora, 'tu salario semanal es de', PagoSemanal)