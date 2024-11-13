print("¡El Comevocales esta hambriento!")

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable palabra_usuario.
palabra_usuario = input("Ingresa una palabra para alimentarlo: ")
palabra_usuario = palabra_usuario.upper()

print("El Comevocales se comio las vocales de tu palabra.")
print("Estos son los restos que dejo:")

for letra in palabra_usuario:
  # Completa el cuerpo del bucle for.
  if letra == "A": continue
  elif letra == "E": continue
  elif letra == "I": continue
  elif letra == "O": continue
  elif letra == "U": continue
  else: print(letra)

