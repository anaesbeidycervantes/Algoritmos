def litres(time):
    # Calcular los litros de agua que Nathan beberá
    # Usar int() para truncar el resultado a un número entero
    return int(time * 0.5)

# Solicitar al usuario el número de horas
time_input = float(input("Ingresa el número de horas que Nathan pasa pedaleando: "))

# Calcular y mostrar la cantidad de litros de agua que Nathan beberá
result = litres(time_input)
print(f"Litros de agua que Nathan beberá: {result} litros")
