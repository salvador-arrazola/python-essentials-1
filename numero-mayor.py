# Almacena el actual número más grande aquí.
numero_mayor = -999999999

# Ingresa el primer valor.
numero = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if numero > numero_mayor:
        # Sí si, se actualiza largest_number.
        numero_mayor = numero
    # Ingresa el siguiente número.
    numero = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", numero_mayor)
