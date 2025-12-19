#declarar variables y pedir datos por consola 
print("Ingrese el precio de 3 productos:")
precio1 = float(input("Precio del producto 1: "))
precio2 = float(input("Precio del producto 2: "))
precio3 = float(input("Precio del producto 3: "))

#aplicar operadores 
total = precio1 + precio2 + precio3

#si compra el primer producto debe pagar el 100%, si compra el segundo producto debe pagar el 70%
#si compra el tercer producto debe pagar el 65%

total *= 0.65

#imprimo el resultado en consola
print(f"El precio total es: $ {total} COP")

