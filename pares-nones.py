# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

nones = 0
pares = 0

# Lee el primer número.
n = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while n: # Equivale a: while n != 0:
    # Verificar si el número es impar.
    if n % 2: # Equivale a: if n % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        nones += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        pares += 1
    # Leer el siguiente número.
    n = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", nones)
print("Conteo de números pares:", pares)
