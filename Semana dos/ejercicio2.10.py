MetrosAPulgadas = 0.0254

def ConvertirMetrosAPulgadas(metros):
    return metros / MetrosAPulgadas

metros = float(input("Ingrese la cantidad de tela en metros: "))

pulgadas = ConvertirMetrosAPulgadas(metros)

print(f"La cantidad de tela en pulgadas es: {pulgadas:.2f}")