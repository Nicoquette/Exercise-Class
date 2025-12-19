'''
el gobierno dara insentibos economicos a la población dependiendo el estrato
estrato 1 1 millón
estrato 2 500 mil
estrato 3 200 mil
estrato 4 0 
estrato 5 impuesto 300 mil
estrato 6 impuesto 600 mil
estrato >6 o <0 error 

ese dinero sera para el pago de matricula en la universidad
'''

#declarar variables y permitir entrada de datos
estrato= int(print("Ingrese su estrato social: "))
valordelamatricula = float(print("Valor de la matrícula: $"))

#Implementar condicionales
if(estrato==1):
    descuento = 1000000
    valordelamatricula = valordelamatricula - descuento
    print("El valor de la matrícula con el descuento aplicado es de: $", valordelamatricula)
elif(estrato == 2):
    descuento = 500000
    valordelamatricula = valordelamatricula - descuento
    print("El valor de la matrícula con el descuento aplicado es de: $", valordelamatricula)
elif(estrato ==3):
    descuento = 200000
    valordelamatricula = valordelamatricula - descuento
    print("El valor de la matrícula con el descuento aplicado es de: $", valordelamatricula)
elif(estrato ==4):
    print("No tiene descuento, el valor de la matrícula es de: $", valordelamatricula)
elif(estrato == 5):
    impuesto = 300000
    valordelamatricula = valordelamatricula + impuesto
    print("El valor de la matrícula con el impuesto aplicado es de: $", valordelamatricula)
elif(estrato == 6):
    valordelamatricula += 600000
    print("El valor de la matrícula con el impuesto aplicado es de: $", valordelamatricula)
else:
    print("Error: Estrato inválido. Por favor ingrese un estrato entre 1 y 6.")