def DeterminarMayor(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

mayor = DeterminarMayor(valor1, valor2)

print(f"El valor mayor es: {mayor}")
