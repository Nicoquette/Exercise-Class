saldo = 5000

historial = []

clave = "1234"

while True: 
    print("---Menu---")
    print("1. Mostrar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial de movimiento ")
    print("5. Cambiar clave")
    print("6. Salir")  
    
    opcion = int(input("Dígite la opción: "))
    
    if opcion == 1:
        print(f"Su saldo es {saldo}")
    elif opcion == 2: 
        retirar= float(input("¿Cuánto quiere retirar? "))
        if retirar <= saldo: 
            saldo -= retirar
            historial.append(f"Retiraste {retirar}")
            print(f"Retiraste $ {retirar}")
            print("Retirado con exito")
            print(f"Su saldo es {saldo}")
        else: 
            print("No hay dinero suficiente en su cuenta")
            print(f"Su saldo es $ {saldo}")
            
    elif opcion ==3:
        depositar= float(input("¿Cuánto desea depositar? "))
        if depositar > 0:
            saldo += depositar
            historial.append(f"Depositaste {depositar}")
            print(f"Deposito exitoso nuevo saldo {saldo}")
        else: 
            print("No es correcta la cantidad, insertar numeros positivos")
            
    elif opcion ==4: 
        print("---Historial---")
        if len(historial) ==0: 
            print("No tiene movimientos")
        else: 
            for movimiento in historial: 
                print(movimiento)
                
    elif opcion == 5:
        intento = input("Escribe tu clave actual: ")
        
        if intento == clave: 
            nueva = input("Escriba la nueva clave: ") 
            clave = nueva
            print("Tu clave ha sido cambiada con exito")
            
        else: 
            print("Clave incorrecta. ")
            
    elif opcion==6: 
        print("Gracias por usar ")
        break
    else:
        print("Error")