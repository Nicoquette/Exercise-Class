'''
La drogueria solo maneja 3 productos fijos en el sistema. 
cada uno tiene su propioNombre, precio y ingreso acomulado
Ver productos disonibles 
Vender cualquiera de los tres productos 
Condultar ingresos totales 
Salir del sistema
'''
p1= "Acetaminofen"
precio1 = 2000
ingreso1 = 0

p2= "Ibuprofeno"
precio2 = 3500
ingreso2 = 0

p3= "Omeprazol"
precio3 = 2000
ingreso3 = 0

def mostrarmenu(): 
    print("\n   Menú Drogueria")
    print("1. Ver productos disponibles ")
    print("2. Vender producto")
    print("3. Consultar ingresos totales ")
    print("3. Salir")
    
def verproducti():
    print("\n Productos disponibles ")
    print(f"1. {p1} - ${precio1}")
    print(f"2. {p2} - ${precio2}")
    print(f"3. {p3} - ${precio3}")
    
def venderproducto():
    global ingreso1, ingreso2, ingreso3
    verproducti()
    opcion = int(input("Ingrese el número del producto a vender: "))
    if opcion == 1:
        cantidad=int(input(f"¿Cuantos {p1} desea vender?: "))
        total= cantidad*precio1
        ingreso1 +=total
        print(f"Venta realizada por ${total}")
    elif opcion ==2:
        cantidad2=int(input(f"¿Cuantos {p2} desea vender?: "))
        total2= cantidad2*precio2
        ingreso2 +=total2
        print(f"Venta realizada por ${total2}")
    elif opcion==3:
        cantidad3=int(input(f"¿Cuantos {p3} desea vender?: "))
        total3= cantidad3*precio3
        ingreso3 +=total3
        print(f"Venta realizada por ${total3}")
    else: 
        print("Error//Opción no valida")
        
def mostraringresos():
    totalIngresos = ingreso1+ingreso2+ingreso3
    print(f"El total de ingresos es igual: ${totalIngresos}")
    print(f"Los ingresos de {p1} es ${ingreso1}")
    print(f"Los ingresos de {p2} es ${ingreso2}")
    print(f"Los ingresos de {p3} es ${ingreso3}")
        
        
while True: 
    mostrarmenu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1: 
        verproducti()
    elif opcion == 2: 
        venderproducto()
    elif opcion == 3:
        mostraringresos()
    elif opcion == 4: 
        print("Gracias por usar nuestro sistema")
        break ##IMPORTANTE PARA SALIR DEL WHILE 
    else: 
        print("Opción invalida")

        
