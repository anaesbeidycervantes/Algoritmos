def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Constante de los gases en dm^3⋅atm⋅K^−1⋅mol^−1
    R = 0.082

    # Convertir la temperatura de Celsius a Kelvin
    T_K = T + 273.15

    # Calcular el número de moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la fórmula
    P_total = (n1 + n2) * R * T_K / V

    return P_total

# Solicitar datos al usuario
M1 = float(input("Ingresa la masa molecular del gas 1 (g/mol): "))
M2 = float(input("Ingresa la masa molecular del gas 2 (g/mol): "))
m1 = float(input("Ingresa la masa presente del gas 1 (g): "))
m2 = float(input("Ingresa la masa presente del gas 2 (g): "))
V = float(input("Ingresa el volumen del recipiente (dm^3): "))
T = float(input("Ingresa la temperatura (°C): "))

# Calcular la presión total
presion = calcular_presion_total(M1, M2, m1, m2, V, T)

# Mostrar el resultado al usuario
print(f"La presión total es: {presion:.2f} atm")
