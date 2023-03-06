monedas = {"USD": 3700, "EUR": 4500, "JPY": 33, "GBP": 5100, "CNY": 570}

intermediacion = {"USD": 0.02, "EUR": 0.03, "JPY": 0.01, "GBP": 0.014, "CNY": 0.015}

nombre = str (input ("Ingrese su nombre : "))
documento = int (input("Ingrese su numero de documento : "))

cantidad = float(input("Ingrese la cantidad de dinero a cambiar: "))
moneda_origen = input("Ingrese la moneda de origen: ").upper()


if moneda_origen not in monedas:
    print("Moneda no existente")
else:
  
    moneda_destino = input("Ingrese la moneda de destino: ").upper()



if moneda_destino not in monedas:
        print("Moneda no existente")
else:
      
        tasa_cambio = monedas[moneda_destino] / monedas[moneda_origen]
        cantidad_destino = cantidad * tasa_cambio

     
        porcentaje_intermediacion = intermediacion[moneda_destino]
        monto_intermediacion = cantidad_destino * porcentaje_intermediacion

if intermediacion > 0.010 : 
      print ("la tasa de cambio supera el 10% ")

cambio_moneda = str(input("Desea hacer el cambio de moneda y mostrar sus datos? ").upper())

if cambio_moneda == "SI":
       print(("su numero de documento es: ").upper(), documento )
       print("La moneda de origen es: ", moneda_origen)
       print("la moneda destino es: ", moneda_destino)
       print(f"La cantidad de {cantidad:.2f} {moneda_origen} equivale a {cantidad_destino:.2f} {moneda_destino}.")
       print(f"Se cobrará un porcentaje de intermediación de {monto_intermediacion:.2f} pesos Colombianos." )

elif cambio_moneda == "NO":
      print (("Su operación ha sido cancelada").upper())