# Ejemplo del uso de str().
cateto_a = float(input("Ingresa la medida del primer cateto: "))
cateto_b = float(input("Ingresa la medida del segundo cateto: "))
# Usa str() para convertir el resultado del calculo de la hipotenusa a cadena y concatenarlo.
print("La hipotenusa resultante es:" + str((cateto_a**2 + cateto_b**2) ** .5))
