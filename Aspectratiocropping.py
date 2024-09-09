import math

def convert_to_16_9(x, y):
    ratio = 16 / 9
    new_x = math.ceil(ratio * y)
    return new_x, y

# Pedimos los valores al usuario
x = int(input("Dame el valor de x: "))
y = int(input("Dame el valor de y: "))

# Calculamos la nueva resolución
new_x, new_y = convert_to_16_9(x, y)

# Explicación sencilla
print("\nExplicación:")
print(f"2. Multiplicamos la altura ({y}) por 1.777 (que es 16/9) para calcular el nuevo ancho.")
print(f"3. Esto nos da un nuevo ancho de {new_x}, y ahora la imagen tiene una resolución de {new_x} × {new_y}.\n")

# Mostramos el resultado
print(f"Original: {x} × {y} -> Convertido a 16:9: {new_x} × {new_y}")
