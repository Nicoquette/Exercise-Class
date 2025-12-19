#declarar variables y pedir variables
Nota1 = float(input("Ingrese la primera nota: "))
Nota2 = float(input("Ingrese la segunda nota: "))
Nota3 = float(input("Ingrese la tercera nota: "))

#implementar operadores
Nota1 *= 0.3
Nota2 *= 0.3
Nota3 *= 0.4
promedio = Nota1 + Nota2 + Nota3

print(f"El promedio final es: {promedio:.2f} ")
