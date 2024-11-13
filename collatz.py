n = int(input("Ingresa un numero mayor que cero: "))
pasos = 0

while True:
  if n % 2 == 0:
    n = n // 2
  else:
    n = 3 * n + 1
  print(n)
  pasos += 1
  if n == 1:
    break

print("Pasos:", pasos)
