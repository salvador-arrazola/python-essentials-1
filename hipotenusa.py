cateto_a = float(input("Ingresa la medida del primer cateto: "))
cateto_b = float(input("Ingresa la medida del segundo cateto: "))
hipotenusa = (cateto_a**2 + cateto_b**2) ** .5
print("La hipotenusa resultante es:", hipotenusa)

# Se puede omitir la variable intermedia "hipotenusa" al hacer el calculo directamente dentro de
# print:
print("La hipotenusa resultante es:", (cateto_a**2 + cateto_b**2) ** .5)
