def nba_extrap(ppg, mpg):
    # Verificar si mpg es 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Calcular los puntos extrapolados a 48 minutos
    extrapolated_ppg = (ppg * 48) / mpg

    # Redondear el resultado a la décima más cercana
    return round(extrapolated_ppg, 1)


# Solicitar al usuario que ingrese los datos
try:
    ppg = float(input("Ingresa el promedio de puntos por juego (ppg): "))
    mpg = float(input("Ingresa el promedio de minutos jugados por juego (mpg): "))

    # Calcular los puntos extrapolados y mostrar el resultado
    result = nba_extrap(ppg, mpg)
    print(f"Si jugara los 48 minutos, el jugador anotaría aproximadamente {result} puntos.")
except ValueError:
    print("Por favor, ingresa números válidos para los puntos y minutos.")
