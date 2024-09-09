#calcula la edad del perro y el gato en años humanos
def calculate_animal_years(human_years):
    # Inicializamos las variables para los años de gato y perro
    cat_years = 0
    dog_years = 0

    # Calculamos los años de gato
    #al primer año el animal tendrá 15 aaños
    if human_years == 1:
        cat_years = 15
    #al segundo año a los 15 años se le sumaran 9 años dando un total de 24
    elif human_years == 2:
        cat_years = 15 + 9
    #al tercer año
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculamos los años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Retornamos la lista con los años humanos, años de gato y años de perro
    return [human_years, cat_years, dog_years]

# Ejemplo de uso
#human_years=15
human_years=int(input("Dame tu edad: "))
#llama a la funcion para los calculos
ages=calculate_animal_years(human_years)
#muesta el resultado y el tipo de datos devueltos por la funcion
print(f"Tu edad es {ages[0]} años.")
print(f"La edad de tu gato es de {ages[1]} años.")
print(f"La edad de tu perro es de {ages[2]} años.")
print(type(ages))

#"Programa que calcula "