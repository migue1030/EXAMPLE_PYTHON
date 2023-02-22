# ejercicio cajero automatico

cliente = str ("erick")
numero_tarjeta = int (65416416463541498)
saldo = float (1534711.75)
retirar = float (120000)
impuesto = (retirar*0.01)
saldo_restante = (saldo-retirar-impuesto)

print ("detalles de su retiro:")
print ("El cliente es", cliente)
print ("con el N° de tarjeta", numero_tarjeta)
print ("saldo actual=", saldo)
print ("desea retirar:", retirar)
print ("impuesto =", impuesto)
print ("saldo restante", saldo_restante)

print ("GRACIAS POR PREFERIRNOS")

