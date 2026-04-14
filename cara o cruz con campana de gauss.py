import random
import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

continuar = True

while continuar:
    limpiar_pantalla()
    print("="*50)
    print("   MONEDA: BARRAS DINÁMICAS POR PORCENTAJE")
    print("="*50)

    try:
        n = int(input("\n¿Cuántas veces quieres lanzar? (0 para salir): "))
        if n == 0: break

        caras = 0
        for i in range(1, n + 1):
            if random.randint(0, 1) == 0:
                caras += 1
            
            # Actualizamos la animación cada N lanzamientos para fluidez
            if i % (max(1, n // 25)) == 0 or i == n:
                limpiar_pantalla()
                
                cruces = i - caras
                porc_cara = (caras / i) * 100
                porc_cruz = (cruces / i) * 100

                print(f"Lanzamiento: {i} / {n}")
                print(f"CARAS: {caras} ({porc_cara:.1f}%) | CRUCES: {cruces} ({porc_cruz:.1f}%)\n")

                # RENDERIZADO DE BARRAS (10 niveles de altura)
                # Cada nivel representa un 10% de probabilidad
                for nivel in range(10, 0, -1):
                    linea = "      "
                    
                    # Lógica para la barra de CARAS
                    if porc_cara >= (nivel * 10):
                        linea += " [█████] "
                    elif porc_cara >= (nivel * 10 - 5): # Relleno medio
                        linea += " [▄▄▄▄▄] "
                    else:
                        linea += " [     ] "

                    linea += "       "

                    # Lógica para la barra de CRUCES
                    if porc_cruz >= (nivel * 10):
                        linea += " [█████] "
                    elif porc_cruz >= (nivel * 10 - 5):
                        linea += " [▄▄▄▄▄] "
                    else:
                        linea += " [     ] "
                    
                    print(linea)

                print("      " + "="*9 + "       " + "="*9)
                print("       CARAS           CRUCES")
                
                # Pausa para el efecto visual
                time.sleep(0.04)

        print("\n¡Simulación completada!")
        input("Presiona Enter para continuar...")

    except ValueError:
        print("Error: Ingresa un número válido.")
        time.sleep(2)

print("¡Gracias por usar el simulador!")