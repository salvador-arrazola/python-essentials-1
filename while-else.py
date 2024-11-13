# Ejecuta el bloque else, despues de terminar el ciclo while.
i = 0
while i < 5:
  print(i)
  i += 1
else:
  print("else:", i)

print("\n"+ "#"*10 + "\n")

# Ejecuta el bloque else, sin haber ingresado al ciclo while.
i = 5
while i < 5:
  print(i)
  i += 1
else:
  print("else:", i)
