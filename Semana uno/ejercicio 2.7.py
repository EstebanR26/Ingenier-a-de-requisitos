def litrosGalones():
    
    litros = float(input("introduzcala cantidad de litros: "))
    galones = litros / 3.785

    return f"su cantidad de litros producida es {galones} galones"
print(litrosGalones()) 