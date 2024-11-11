print("Millas a Kilómetros | Kilómetros a Millas:")

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, "millas son", round(millas_a_kilometros, 2), "kilómetros.")
print(kilometros, "kilómetros son", round(kilometros_a_millas, 2), "millas.")
print()

print("Dolares a Pesos | Pesos a Dolares:")

dolares = 235.85
pesos = 4950

dolares_a_pesos = dolares * 20.85
pesos_a_dolares = pesos / 20.85

print("$", dolares, " USD equivalen a $", round(dolares_a_pesos, 2), " MXN.", sep="")
print("$", pesos, " MXN equivalen a $", round(pesos_a_dolares, 2), " USD.", sep="")
print()

print("Fahrenheit a Celsius | Celsius a Fahrenheit:")

fahrenheit = 41.8
celsius = 35.4

fahrenheit_a_celsius = (fahrenheit - 32) * (5 / 9)
celsius_a_fahrenheit = (celsius * (9/5)) + 32

print(fahrenheit, "°F", " equivalen a ", round(fahrenheit_a_celsius, 1), "°C.", sep="")
print(celsius, "°C", " equivalen a ", round(celsius_a_fahrenheit, 1), "°F.", sep="")
