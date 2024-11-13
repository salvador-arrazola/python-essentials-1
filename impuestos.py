ingreso_anual = float(input("Introduce el ingreso anual: "))

if ingreso_anual <= 85528:
	impuesto = ingreso_anual * 0.18 - 556.02
# Escribe tu código aquí.
else:
	impuesto = 14839.02 + (ingreso_anual - 85528) * 0.32

impuesto = round(impuesto, 0)

if impuesto < 0:
	impuesto = 0;

print("El impuesto es: $", impuesto, " pesos", sep="")
 