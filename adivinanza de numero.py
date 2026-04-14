numero_secreto=15
numero_elegido=int(input("Introduzca un numero del 1 al 50: "))
while numero_elegido != numero_secreto:
    print("El numero elegido no es correcto, intente de nuevo")
    if numero_elegido < numero_secreto:
        print("El numero elegido es menor al numero secreto")
        
    else: 
         print("El numero elegido es mayor al numero secreto")

    numero_elegido=int(input("Introduzca un numero del 1 al 50: "))
print("Felicidades, has adivinado el numero secreto")
