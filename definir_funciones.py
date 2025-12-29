def calcular_area(base:float,altura: float)-> float:
    return(base*altura)

area1=calcular_area(5,10)
print(f"El área del rectángulo es: {area1}")


def menu ():
    print("menu")
    print("1. Opción 1")
    print("2. Opción 2")        
    
    
        
#FUNCIONAES ANONIMAS 
calcularAreaRectangulo= lambda base, altura: base * altura #calcular area de un rectangulo
area2=calcularAreaRectangulo(7,3)
print(f"El área del rectángulo es: {area2}")

#lista

mis_numeros=[1,2,3,4,5,6,7,8,9,10]
mis_numeros[0]=20
print(mis_numeros)


#Tupla

mitupla=(1,2,3,4,5)
print(mitupla[0])
#mitupla[0]=20 #no se puede modificar una tupla

#DICCIONARY

mydiccionary = {
    "Clave1": 1,
    "Clave2": 2,
    "Clave3": 3,
}

mydiccionary["Clave1"]=20
print(mydiccionary["Clave1"])
#Mini prueba
