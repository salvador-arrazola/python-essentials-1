# Imprime los numeros del 0 al 9:
for i in range(10):
  print("El valor de i es", i)

print("\n"+ "#"*20 + "\n")

# Imprime los numeros del 2 al 7:
for i in range(2, 8):
  print("El valor de i es", i)

print("\n"+ "#"*20 + "\n")

# Imprime los numeros del 2 al 7, pero saltando de 3 en 3, es decir solo imprime 2 y 5:
for i in range(2, 8, 3):
  print("El valor de i es", i)

print("\n"+ "#"*20 + "\n")

# No imprime ningun numero, debido a que la funcion range() no incluye el valor final:
for i in range(1, 1):
  print("El valor de i es", i)

print("\n"+ "#"*20 + "\n")

# No imprime ningun numero, debido a que el valor inicial de la funcion range() es mayor al valor
# final:
for i in range(2, 1):
  print("El valor de i es", i)
