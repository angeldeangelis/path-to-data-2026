import random

continuar = True

while continuar == True:
    print("\n--- Bienvenido al simulador de lanzamiento de moneda ---")

    try:
        n = int(input("Ingrese el número de veces (0 para salir): "))
        
        # Filtro 1: Si el usuario pone 0 para salir
        if n == 0:
            print("Saliendo del programa...")
            continuar = False
            continue # Regresa al while, ve que continuar es False y termina

        # Filtro 2: Si el usuario pone un número negativo
        if n < 0:
            print("Debe ingresar un número mayor a cero.")
            continue # Regresa al inicio para preguntar otra vez

        # --- TODO LO DE ABAJO SOLO PASA SI N ES VÁLIDO ---
        contador_cara = 0
        contador_cruz = 0

        for i in range(n):
            resultado = random.randint(0, 1)
            if resultado == 0:
                contador_cara += 1
            else:
                contador_cruz += 1

        # Mostramos resultados
        porcentaje_cara = (contador_cara / n) * 100
        porcentaje_cruz = (contador_cruz / n) * 100
        
        print(f"Resultados: Cara: {contador_cara}, Cruz: {contador_cruz}")
        print(f"Porcentaje de Cara: {porcentaje_cara:.2f}%, Cruz: {porcentaje_cruz:.2f}%")

    except ValueError:
        print("Error: Debes ingresar un número entero.")
        # No hace falta poner continuar=False aquí, 
        # mejor dejar que el usuario lo intente de nuevo.

print("\nGracias por usar el simulador. ¡Hasta luego!")