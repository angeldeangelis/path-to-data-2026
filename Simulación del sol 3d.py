from vpython import sphere, color, rate, vector, curve, scene

# 1. Configuración de la Escena (Vista mejorada)
scene.title = "Curvatura Espacio-Tiempo: El Sol"
scene.width = 1000
scene.height = 700
scene.background = vector(0.01, 0.01, 0.05)

# --- TRUCO DE CÁMARA ---
# Ajustamos el centro y la dirección hacia donde mira el "ojo"
scene.range = 12
scene.forward = vector(-1, -1, -1) # Mira hacia abajo y en diagonal
scene.up = vector(0, 1, 0)         # Define qué es "arriba"

# 2. El Sol
sol = sphere(pos=vector(0,0,0), radius=1.8, color=color.orange, 
             emissive=True, shininess=1)

# 3. CREACIÓN DE LA MALLA LIGERA (Menos hilos)
# Usaremos 'curve' para dibujar líneas en lugar de superficies sólidas
distancia_max = 10
espaciado = 1 # Aumentar este número reduce la cantidad de hilos

def calcular_y(x, z):
    # Fórmula de curvatura: El hundimiento aumenta cerca del centro (0,0)
    d = vector(x, 0, z).mag
    if d < 0.1: d = 0.1
    return -4 / (d + 1.2) # Ajusta el -4 para hundir más o menos

# Dibujamos líneas horizontales (Eje X)
for z in range(-distancia_max, distancia_max + 1, espaciado):
    linea = curve(color=color.cyan, radius=0.03, opacity=0.6)
    for x in range(-distancia_max, distancia_max + 1):
        linea.append(vector(x, calcular_y(x, z), z))

# Dibujamos líneas verticales (Eje Z)
for x in range(-distancia_max, distancia_max + 1, espaciado):
    linea = curve(color=color.cyan, radius=0.03, opacity=0.6)
    for z in range(-distancia_max, distancia_max + 1):
        linea.append(vector(x, calcular_y(x, z), z))

# 4. Simulación
print("Usa el CLIC DERECHO para rotar la cámara y la RUEDA para el zoom.")

while True:
    rate(30)
    # Hacemos que el sol rote sobre sí mismo para que se vea vivo
    sol.rotate(angle=0.01, axis=vector(0,1,0))