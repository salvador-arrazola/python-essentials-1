print("Prioridad de operadores diferentes:")
print(2 + 3 * 5)
print(2 * 3 % 5)
print()

print("Prioridad (enlace) de operadores con la misma prioridad:")
print("- Modulo: izq > der.")
print(9 % 6 % 2)
print("- Exponente: der > izq.")
print(2 ** 2 ** 3)
print()

print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))
print()

print("Prioridades:")
print("1) **")
print("2) +, - (unario)")
print("3) *, /, //, %")
print("4) +, -")
print()

print("Agrupacion con parentesis:")
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)