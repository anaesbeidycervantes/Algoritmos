import math  # Importa el módulo de matemáticas para usar funciones matemáticas


def age_range(age):
    if age > 14:
        min_age = math.floor(age / 2 + 7)  # Calcula la edad mínima y redondea hacia abajo
        max_age = math.floor(age * 2 - min_age)  # Calcula la edad máxima y redondea hacia abajo
    else:
        min_age = math.floor(age - 0.10 * age)  # Calcula la edad mínima y redondea hacia abajo
        max_age = math.floor(age + 0.10 * age)  # Calcula la edad máxima y redondea hacia abajo

    return f"{min_age}-{max_age}"


# Solicitar al usuario su edad
age = int(input("Ingresa tu edad: "))

# Llamar a la función y mostrar el resultado
print(age_range(age))
