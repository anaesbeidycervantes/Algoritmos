#El programa indica el precio del mango que saldria segun la promocion que se esta indicando el porblema
def mango(quantity, price):
    # Calcular el número de grupos de 3 mangos
    free_groups = quantity // 3
    # Calcular el número de mangos que se pagan
    pay_mangos = quantity - free_groups
    # Calcular el costo total
    total_cost = pay_mangos * price
    return total_cost

# Solicitar al usuario el número de mangos
quantity = int(input("Ingresa el número de mangos: "))

# Solicitar al usuario el precio por mango y validar que no sea menor a 10
while True:
    price = float(input("Ingresa el precio por mango (debe ser al menos 10): "))
    if price >= 10:
        break
    else:
        print("El precio debe ser al menos 10. Por favor, ingresa un precio válido.")

# Calcular el costo total usando la función mango
total_cost = mango(quantity, price)

# Mostrar el resultado al usuario
print(f"El costo total de {quantity} mangos a ${price:.2f} por mango es: ${total_cost:.2f}")
