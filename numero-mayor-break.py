numero_mayor = -99999999
contador = 0

while True:
  n = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
  if n == -1:
    break
  contador += 1
  if n > numero_mayor:
    numero_mayor = n

if contador != 0:
  print("El número más grande es", numero_mayor)
else:
  print("No has ingresado ningún número.")
