accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "Me estoy registrando"

#Estructura de control (condicional o sentencia if o si)
#Permite continuar un flujo (realizar algo) si se cumple una condicion
#  y en caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa)
# esta sentencia (condicional if) va acompañado de los operadores de comparacion 
"""
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno != estructura_datos_dos
"""

#Hay varias maneras de utilizar la sentencia if
#if simple, if compuesto, if anidado

#if simple
dato_comparacion = 18
edad = 20
"""if edad >= dato_comparacion:
    print("Ingresar, difrutar del evento")
"""

 #if compuesto
"""if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")
"""
boleta = True
fecha_event = "28-02-2023"
fecha_comparacion = "28-02-2023"
#if anidado
if edad >= dato_comparacion and boleta and fecha_event == fecha_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")

opciones = """
Localidades 
1- VIP
2- Preferencial
3-General
4-Baja
"""
print(opciones)

op = int (input("Escoja una opcion"))

if op is 1:
    print("Precio $500")
elif op is 2:
    print("Precio $400")
elif op is 3:
    print("Precio $200")
elif op is 4:
    print("Precio $100")