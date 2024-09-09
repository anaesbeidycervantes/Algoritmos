#El programa calcula el valor del 3er angulo interno de cualquier trinagulo
def third_angle(angle1, angle2):
    # Validar que los ángulos sean mayores a 0 y menores a 180
    if angle1 <= 0 or angle2 <= 0:
        return "Los ángulos deben ser mayores que 0."

    # Validar que la suma de los dos ángulos sea menor que 180
    if angle1 + angle2 >= 180:
        return "Los ángulos ingresados no forman un triángulo válido."

    # Si los ángulos son válidos, calculamos el tercer ángulo
    return 180 - (angle1 + angle2)


# Solicitar al usuario que ingrese los valores de los dos ángulos
angle1 = int(input("Ingresa el primer ángulo: "))
angle2 = int(input("Ingresa el segundo ángulo: "))

# Llamamos a la función con los ángulos proporcionados por el usuario
third = third_angle(angle1, angle2)

# Mostrar el tercer ángulo o el mensaje de error
print(third)
