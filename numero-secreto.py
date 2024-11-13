numero_secreto = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero_usuario = int(input("Adivina el numero secreto: "))

while numero_usuario != numero_secreto:
  print("¡Ja, ja! ¡Estás atrapado en mi bucle!\n")
  numero_usuario = int(input("Adivina el numero secreto: "))

print("\n¡No lo puedo creer! Adivinaste el numero secreto:", numero_secreto)
print("¡Bien hecho, muggle! Eres libre ahora.")
