empleados = ["Empleado_1","Empleado_2","Empleado_3","Empleado_4"]
horas_diarias = int("8")
dias_mes= int (30)
dias_extras = int(10)
proyectos = {
	"Proyecto A Sueldo": int(20000),
	"Proyecto B Sueldo": int (10000),
	"Proyecto C Sueldo": int (5000), 
}
print ("")
print ("El", empleados[0], "trabaja", horas_diarias, "horas,", "en el proyecto 'A',", "cobrando", proyectos ["Proyecto A Sueldo"], "la Hora" )
print ("El", empleados[1], "trabaja", horas_diarias, "horas,", "en el proyecto 'B',", "cobrando", proyectos ["Proyecto B Sueldo"], "la Hora")
print ("El", empleados[2], "trabaja", horas_diarias, "horas,", "en el proyecto 'C',", "cobrando", proyectos ["Proyecto C Sueldo"], "la Hora")
print ("El", empleados[3], "trabaja", horas_diarias, "horas,", "en el proyecto 'A',", "cobrando", proyectos ["Proyecto A Sueldo"],  "la Hora")
print ("")

sueldo_empleado1 = (horas_diarias * dias_mes * proyectos["Proyecto A Sueldo"])
sueldo_empleado2 = (horas_diarias * dias_mes * proyectos["Proyecto B Sueldo"])
sueldo_empleado3 = (horas_diarias * dias_mes * proyectos["Proyecto C Sueldo"])
sueldo_empleado4 = (horas_diarias * dias_mes * proyectos["Proyecto A Sueldo"])

print ("El sueldo mensual del", empleados[0], "es de:", sueldo_empleado1,"$")
print ("El sueldo mensual del", empleados[1], "es de:", sueldo_empleado2,"$")
print ("El sueldo mensual del", empleados[2], "es de:", sueldo_empleado3,"$")
print ("El sueldo mensual del", empleados[3], "es de:", sueldo_empleado4,"$")
print ("")

dato_comparacion = int (1500000)
valor_extra = float(0.06   )
Horas_extra = int(3)
if sueldo_empleado1 > dato_comparacion:
 print ("El salario del", empleados[0], "Es mayor al tope maximo")
else: 
    Pago_total = (proyectos["Proyecto A Sueldo"] * Horas_extra * valor_extra * dias_mes)
    print ("el pago del", empleados[0], "es de", Pago_total + sueldo_empleado1,"- Su salario incrementó un 6%", "trabajando 10 dias, 3 horas extras")
    

if sueldo_empleado2 > dato_comparacion:
 print ("El salario del", empleados[1], "Es mayor al tope maximo")
else: 
    Pago_total = (proyectos["Proyecto B Sueldo"] * Horas_extra * valor_extra * dias_extras )
    print ("el pago del", empleados[1], "es de", Pago_total + sueldo_empleado2,"- Su salario incrementó un 6%", "trabajando 10 dias, 3 horas extras")


if sueldo_empleado3 > dato_comparacion:
 print ("El salario del", empleados[2], "Es mayor al tope maximo")
else: 
    Pago_total = (proyectos["Proyecto C Sueldo"] * Horas_extra * valor_extra * dias_extras)
    print ("el pago del", empleados[2], "es de", Pago_total + sueldo_empleado3,"- Su salario incrementó un 6%", "trabajando 10 dias, 3 horas extras" )
    

if sueldo_empleado4 > dato_comparacion:
 print ("El salario del", empleados[3], "Es mayor al tope maximo")
else: 
    Pago_total = (proyectos["Proyecto A Sueldo"] * Horas_extra * valor_extra )
    print ("el pago del", empleados[3], "es de", Pago_total + sueldo_empleado4,"- Su salario incrementó un 6%", "trabajando 10 dias, 3 horas extras")
   