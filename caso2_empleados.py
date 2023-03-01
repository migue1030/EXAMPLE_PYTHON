empleados = ["Empleado_1","Empleado_2","Empleado_3","Empleado_4"]
horas_diarias = int("8")
proyectos = {
	"Proyecto A Sueldo": int(20000),
	"Proyecto B Sueldo": int (10000),
	"Proyecto C Sueldo": int (5000), 
}
print ("El empleado denominado:", empleados[0], "Trabaja", horas_diarias, "horas,", "en el proyecto 'A',", "cobrando", proyectos ["Proyecto A Sueldo"], "la Hora" )
print ("El empleado denominado:", empleados[1], "Trabaja", horas_diarias, "horas,", "en el proyecto 'B',", "cobrando", proyectos ["Proyecto B Sueldo"], "la Hora")
print ("El empleado denominado:", empleados[2], "Trabaja", horas_diarias, "horas,", "en el proyecto 'C',", "cobrando", proyectos ["Proyecto C Sueldo"], "la Hora")
print ("El empleado denominado:", empleados[3], "Trabaja", horas_diarias, "horas,", "en el proyecto 'A',", "cobrando", proyectos ["Proyecto A Sueldo"],  "la Hora")

sueldo_empleado1 = (horas_diarias * 30 * proyectos["Proyecto A Sueldo"])
sueldo_empleado2 = (horas_diarias * 30 * proyectos["Proyecto B Sueldo"])
sueldo_empleado3 = (horas_diarias * 30 * proyectos["Proyecto C Sueldo"])
sueldo_empleado4 = (horas_diarias * 30 * proyectos["Proyecto A Sueldo"])

print ("El sueldo mensual del", empleados[0], "es de:", sueldo_empleado1,"$")
print ("El sueldo mensual del", empleados[1], "es de:", sueldo_empleado2,"$")
print ("El sueldo mensual del", empleados[2], "es de:", sueldo_empleado3,"$")
print ("El sueldo mensual del", empleados[3], "es de:", sueldo_empleado4,"$")


dato_comparacion = int (1500000)
valor_extra = int (6)
Horas_extra = int(3)
if sueldo_empleado1 > dato_comparacion:
 print ("El salario del", empleados[0], "Es mayor al tope maximo")
else: 
    Horas_extra = int(3)
    Pago_total = (proyectos["Proyecto A Sueldo"] * Horas_extra * valor_extra / 100)
    print("el salario extra es de", Pago_total)
    print ("el pago del", empleados[0], "es de", Pago_total + sueldo_empleado1,"- Su salario incrementó un 6%", "con 3 horas extra"  )
    

if sueldo_empleado2 > dato_comparacion:
 print ("El salario del", empleados[1], "Es mayor al tope maximo")
else: 
    Pago_total = (proyectos["Proyecto B Sueldo"] * Horas_extra * valor_extra / 100)
    print("el salario extra es de", Pago_total)
    print ("el pago del", empleados[1], "es de", Pago_total + sueldo_empleado2,"- Su salario incrementó un 6%", "con 3 horas extra"  )


if sueldo_empleado3 > dato_comparacion:
 print ("El salario del", empleados[2], "Es mayor al tope maximo")
else: 
    
    Pago_total = (proyectos["Proyecto C Sueldo"] * Horas_extra * valor_extra / 100)
    print ("el pago del", empleados[2], "es de", Pago_total + sueldo_empleado3,"- Su salario incrementó un 6%", "con 3 horas extra"  )
    

if sueldo_empleado4 > dato_comparacion:
 print ("El salario del", empleados[3], "Es mayor al tope maximo")
else: 
    
    Pago_total = (proyectos["Proyecto A Sueldo"] * Horas_extra * valor_extra / 100)
    print ("el pago del", empleados[3], "es de", Pago_total + sueldo_empleado4,"- Su salario incrementó un 6%", "con 3 horas extra" )