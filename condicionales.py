#  CONDICIONALES EN PYTHON
#IF(CONDICION):
#    INSTRUCCIONES
#ELSE:
#    INSTRUCCIONES

numero= int(input("Ingrese un numero: "))

#tomar decisiones
if(numero == 0):
    print("El numero es nulo")
elif(numero > 0): 
    print("El numero es positivo")
else:
    print("El numero es negativo")
