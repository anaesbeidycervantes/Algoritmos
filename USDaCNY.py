def usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75

    # Convertir USD a CNY
    cny = usd * conversion_rate

    # Formatear el resultado a 2 decimales y añadir 'Chinese Yuan'
    result = f"{cny:.2f} Chinese Yuan"

    return result

# Solicitar al usuario el monto en USD
print("Se sabe que 1 USd equivale a 6.75 CNY")
usd_amount = float(input("\nIngresa el monto en USD que deseas convertir a CNY: "))

# Convertir el monto ingresado a CNY
conversion_result = usd_to_cny(usd_amount)

# Mostrar el resultado al usuario
print(conversion_result)
