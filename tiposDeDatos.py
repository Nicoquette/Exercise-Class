#declara variables y pedir datos por teclado 
edad= int(input("¿Cuál es tu edad?"))
salario = float(input("Cuál es tu salario"))
nombre = input("Cuál es tu nombre")

#salida de datos 
print("tu edad es ", edad )
print("tu salario es ", salario )
print("tu nombre es ", nombre )
print(f"tu sueldo es {salario:.0f}")  #f-string con formato para salario sin decimales