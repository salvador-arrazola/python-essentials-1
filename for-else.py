# Ejecuta el bloque else, despues de terminar el ciclo for (i conserva el ultimo valor).
for i in range(5):
  print(i)
else:
  print("else:", i)

print("\n"+ "#"*10 + "\n")

# Ejecuta el bloque else, sin ingresar al ciclo for (i conserva el valor antes del ciclo).
i = 100
for i in range(2, 1):
  print(i)
else:
  print("else:", i)
