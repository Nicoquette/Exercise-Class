'''
CONDCIONAL SIMPLE


edad = int(input("Ingrese la edad: "))

if edad> 18:
    print("Eres mayor de edad")
    
#CONDICIONAL COMPUESTA 
nota = float(print("Ingrese la nota: "))
if nota>3:
    print("Aprobaste")
else: 
    print("Reprobaste")
    
    
#Condicional multiple 
nota = float(input("Ingrese la nota"))
if nota >= 0 and nota <= 3 : 
    print("reprobaste")
elif nota >= 3 and nota <= 5: 
    print("Aprobaste")
else:
    print("error")
    
'''

#Condicional anidada
usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")

if usuario == "Pepito":
    if clave == "ADMN":
        print("Bienvenido")
    else: 
        print("Password invalue")
else: 
    print("Usuario no encontrado")
    

    
