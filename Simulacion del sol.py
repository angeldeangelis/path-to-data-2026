import os
import time

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- CONFIGURACIÓN INICIAL ---
hidrogeno = 100.0   # Porcentaje de combustible
edad = 4.6          # En miles de millones de años
temperatura = 5500  # Grados Celsius
estado = "Secuencia Principal"
sistema_solar = True

while sistema_solar:
    limpiar()
    
    # Dibujamos un sol simple con texto
    print("      .    * .    * .  ")
    print("   * _---_    .    * ")
    print("  .   /       \   * .  ")
    print(f" * |   {estado[0]}   |  .   * ") # Muestra la inicial del estado
    print("  .   \_     _/  .    * ")
    print("   * ---    * .    * ")
    
    print("\n--- ESTADO DEL SOL ---")
    print(f"Edad: {edad:.2f} mil millones de años")
    print(f"Combustible (H): {hidrogeno:.2f}%")
    print(f"Temperatura: {temperatura} °C")
    print(f"Fase Actual: {estado}")
    print("-" * 25)

    # --- LÓGICA DE LA SIMULACIÓN ---
    # En cada "vuelta", el sol envejece y consume hidrógeno
    time.sleep(0.5) # Velocidad de la simulación
    edad += 0.1
    hidrogeno -= 1.5

    # --- EVENTOS SEGÚN EL COMBUSTIBLE ---
    if hidrogeno <= 50 and hidrogeno > 20:
        estado = "Estrella Estable (Envejeciendo)"
        temperatura += 10
        
    elif hidrogeno <= 20 and hidrogeno > 0:
        estado = "GIGANTE ROJA (Expandiéndose)"
        temperatura = 3000 # Las gigantes rojas son más frías pero enormes
        
    elif hidrogeno <= 0:
        estado = "ENANA BLANCA (Colapso)"
        temperatura = 10000 # Muy caliente pero pequeña
        hidrogeno = 0
        print("\n¡El Sol se ha quedado sin combustible!")
        print("La Tierra ha sido consumida. Fin de la simulación.")
        sistema_solar = False # Detiene el bucle

print("\nSimulación finalizada.")