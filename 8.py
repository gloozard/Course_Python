from math import sqrt



def calculadora():
    accion= None



    while accion != 0:
        print("\n------>Bienvenido a la calculadora<-------\n")
        print("1) Suma")
        print("2) Resta")
        print("3) Multipplicacion")
        print("4) Division")
        print("5) Raiz cuadrada")
        print("6) potencia")
        print("7) serie de fibonacci")
        print("0) Salir")



        accion=input("Que accion te gustaria realizar: ")



        if accion == "1":
            num=input("Numero 1 -> ")
            num2=input("Numero 2-> ")
            num=float(num)
            num2=float(num2)

            print(f"La suma del numero {num} y {num2} es: ", num+num2, "\n") 

        elif accion == "2":
            num=input("Numero 1 -> ")
            num2=input("Numero 2-> ")
            num=float(num)
            num2=float(num2)

            print(f"La resta del numero {num} y {num2} es: ", num-num2, "\n") 
        
        elif accion == "3":
            num=input("Numero 1 -> ")
            num2=input("Numero 2-> ")
            num=float(num)
            num2=float(num2)

            print(f"La multiplicacion del numero {num} y {num2} es: ", num*num2, "\n")

        elif accion == "4":
            num=input("Numero 1 -> ")
            num2=input("Numero 2-> ")
            num=float(num)
            num2=float(num2)

            print(f"La division del numero {num} y {num2} es: ", num/num2, "\n")

        elif accion == "5":
            num=input("Numero 1 -> ")
            num=float(num)

            print(f"La raiz cuadrada del numero {num} es: ", sqrt(num), "\n")   
        
        elif accion == "6":
            num=input("Numero 1 -> ")
            num2=input("Numero 2-> ")
            num=float(num)
            num2=float(num2)

            print(f"El resultado del {num} a la {num2} potencia es: ", num**num2, "\n") 

        elif accion =="7":
            num=input("Hasta que numero quieres que te haga la funcion de fibonacci -> ")
            num=int(num)
            
            resultado=0
            numero=0
            numero2=0


            for i in range(num):

                resultado = numero +numero2

                if resultado > 0:
                    numero2 = numero
                    numero = resultado
                    print(resultado)
                    
                else:
                    numero+=1
                    print(resultado)


  

                

        
        elif accion=="0":
            print("\nAdios!!!")
            
            return

        else:
            print("Selecciona una opcion valida!!!\n")    
    

    

calculadora()