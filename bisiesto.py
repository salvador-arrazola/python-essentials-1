year = int(input("Introduce un año: "))

if year < 1582:
	print(year, "no esta dentro del período del calendario Gregoriano.")
else:
    #  Escribe el bloque if-elif-elif-else aquí.
  if year % 4 != 0:
    print(year, "es un AÑO COMUN.")
  elif year % 100 != 0:
    print(year, "es un AÑO BISIESTO.")
  elif year % 400 != 0:
    print(year, "es un AÑO COMUN.")
  else:
    print(year, "es un AÑO BISIESTO.")
