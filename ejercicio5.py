#declarar variables y pedir datos por cnsola 
print("Ingrese la produccion por cada turno")

turno1 = float(input("Produccion del turno 1:"))
turno2= float(input("Produccion del turno 2:"))

#implementar operadores 
diferencia = turno1 - turno2
print(f"La diferencia de produccion es {diferencia}")
print("si el resultado es negativo, el turno 2 produjo mas que el turno 1")
print("si el resultado es positivo, el turno 1 produjo mas que el turno 2")
print("si el resultado es 0, ambos turnos produjeron igual")