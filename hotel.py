TARIFAS = {
    'INDIVIDUAL': 2500,
    'DOBLE': 4600,
    'FAMILIAR': 5200
}

DESCUENTOS = {
    1: 0.05,
    2: 0.09,
    3: 0.15
}

def calcular_precio(cantidad_huespedes, dias_estadia):
    if cantidad_huespedes == 1:
        tarifa = TARIFAS['INDIVIDUAL']
    elif cantidad_huespedes == 2:
        tarifa = TARIFAS['DOBLE']
    else:
        tarifa = TARIFAS['FAMILIAR']
    
    precio_sin_descuento = dias_estadia * tarifa
    descuento = precio_sin_descuento * DESCUENTOS.get(cantidad_huespedes, 0)
    precio_con_descuento = precio_sin_descuento - descuento
    
    return precio_con_descuento

cantidad_huespedes = int(input('Ingrese la cantidad de huéspedes: '))
dias_estadia = int(input('Ingrese la cantidad de días que estará: '))

precio_final = calcular_precio(cantidad_huespedes, dias_estadia)

print('El precio final a cobrar es:', precio_final)