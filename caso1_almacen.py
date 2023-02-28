articulo = ["zapatos", "tenis", "camisetas", "jeans"]
precio_venta = [350000, 280000, 175000, 200000]
costo_total = precio_venta[0]+ precio_venta[1]+ precio_venta[2]+ precio_venta[3]
aumento_jeans = float (0.062 * precio_venta[3] + precio_venta[3])
precio_zapatos = float (precio_venta[0]- 0.008 * precio_venta[0])

print(articulo[0],"cuestan: $", precio_venta[0])
print(articulo[1],"cuestan: $", precio_venta[1])
print(articulo[2],"cuestan: $", precio_venta[2])
print(articulo[3],"cuestan: $",precio_venta[3])

print ("costo total de todos los productos = $", costo_total)

print("nuevo costo de jeans")
print("antes: $", precio_venta[3])
print("ahora: $", aumento_jeans)

print ("nuevo costo de zapatos:")
print ("antes: $", precio_venta[0])
print ("ahora: $", precio_zapatos)