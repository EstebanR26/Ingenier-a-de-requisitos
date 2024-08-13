class ejemplo1:

    def calcular_area(A, B, C, base):

     # Calculamos el área de la Forma A
     area_forma_a = (A - C) * B / 2
    
    # Calculamos el área de la Forma B
     area_forma_b = area_forma_a + (C * base)
     return area_forma_a, area_forma_b

    # Ejemplo de uso:
    A_valor = 10  # Reemplazar con el valor real de A
    B_valor = 5   # Reemplazar con el valor real de B
    C_valor = 6   # Reemplazar con el valor real de C
    base_valor = 4  # Reemplazar con el valor real de la base para Forma B
    
    area_forma_a_resultado, area_forma_b_resultado = calcular_area(A_valor, B_valor, C_valor, base_valor)
    print("Área de Forma A:", area_forma_a_resultado)
    print("Área de Forma B:", area_forma_b_resultado)
