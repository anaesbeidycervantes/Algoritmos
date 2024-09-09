#Este programa redondea numeros flotantes con 2 decimales
def redondear_a_dos_decimales(numero):
    return round(numero, 2)

# Solicitar al usuario que ingrese un número
entrada_usuario = float(input("Ingresa un número para redondear a dos decimales: "))

# Redondear el número ingresado
resultado = redondear_a_dos_decimales(entrada_usuario)

# Mostrar el resultado
print(f"El número redondeado a dos decimales es: {resultado}")
