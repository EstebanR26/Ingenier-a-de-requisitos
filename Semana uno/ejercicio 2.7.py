class ejemplo2:
    def calcular_pago(litros_producidos):
        galones_entregados = litros_producidos / 3.785
        precio_por_galon = 10  # Supongamos un precio de $10 por galón
        pago_total = galones_entregados * precio_por_galon
        return pago_total
    
    print(f"El productor recibirá ${pago_hoy:.2f} por la entrega de hoy.")