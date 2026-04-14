def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value"
    if n < 1:
        return "Argument must be an integer greater than 0"
    
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    return " ".join(result)

# --- PRUEBA EN TERMINAL ---
# Aquí es donde llamas a la función para verla en VS Code
numero = int(input("Ingrese un número entero: "))

print(number_pattern(numero))