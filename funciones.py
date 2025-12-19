#Declarar funciones con parametros
#def saludar(nombre):
#    print(f"Hola {nombre}")

#Funciones con retorno de valor 
'''def sumar(num1, num2):
    return num1 + num2

resultado = sumar(10,8)
print(f"La suma es {sumar}")'''
'''
def sumar_hasta_100():
    total = 0
    for i in range(0,101):
        total += i
    return total

resultado = sumar_hasta_100()
print(f"La suma de 1 a 100 es: {resultado}")
'''
'''
def validarpass():
    password = "Dev"
    intentos= 0 
    
    while intentos < 3: 
        entrada = input("Ingrese el password: ")
        if entrada == password:
            print("Bienvenido")
        else: 
            print("Contraseña incorrecta")
            intentos += 1
            print(f"Te quedan {3-intentos} intentos")
            
    print("Has excedido el número de intento")

validarpass()'''

def tablasMultiplicar(numero):
    for i in range(1,11): 
        resultado = numero*i
        print(f"{numero} X {i} ={resultado}")
        
numero = int(input("Ingresa el número: "))
tablasMultiplicar(numero)