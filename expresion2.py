horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
minutos_inicio = (horas * 60) + minutos
minutos_final_total = minutos_inicio + duracion
hora_final = (minutos_final_total // 60) % 24
minutos_final = minutos_final_total % 60

print("El evento finalizará a las ", hora_final, ":", minutos_final, sep="")
