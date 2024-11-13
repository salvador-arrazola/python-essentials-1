print("¡El Comevocales esta hambriento!")

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable palabra_usuario.
palabra_usuario = input("Ingresa una palabra para alimentarlo: ")
palabra_usuario = palabra_usuario.upper()
letras_restantes = ""

for letra in palabra_usuario:
  # Completa el cuerpo del bucle for.
  if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U": continue
  else: letras_restantes += letra

print("El Comevocales se comio las vocales de tu palabra.")
print("Estos son los restos que dejo:", letras_restantes)
