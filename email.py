username = ""
for c in "john.smith@pythoninstitute.org":
  if c == "@":
    break
  username += c
print("El username en john.smith@pythoninstitute.org es: "+ username)
