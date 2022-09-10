# Programa que permita crear dos listas de distintas longitudes
# Que la longitud y los elementos de cada lista sean especificados por el usuario
# Que imprima las listas indicando que son las listas originales
# Que elimine de la primera lista los nombres de la segunda
# Que imprima la primera lista indicando que se han eliminado los elementos que estaban tambien en la segunda

def agregar_datos(lista, elementos):
    """
    Funcion que solicita al usuario una lista y un numero de elementos a agregar
    """
    # if valor == ' ':
    #     valor = 'No especificado'
    # lista.append(valor)

    for i in range(elementos):
        valor = input('Ingrese el elemento {}: '.format(i + 1)).title()
        lista.append(valor)

    return lista


def comparar_listas(lista1, lista2):
    """
    Funcion que compara elementos de ambas listas y encuentra los elementos que se repiten
    """
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    return list(conjunto1 & conjunto2)


def array_diff(lista1, lista2):
    """
    Funcion que extrae los elementos comunes entre la lista 1 y la lista 2 de la lista 1 y los imprime
    """
    return [i for i in lista1 if i not in lista2]


lista1 = []
lista2 = []

nombres1 = int(input('¿Cuantos elementos desea registrar en la lista 1?: '))

agregar_datos(lista1, nombres1)

nombres2 = int(input('¿Cuantos elementos desea registrar en la lista 2?: '))

agregar_datos(lista2, nombres2)

print('Las listas originales son:')
print(f'La lista 1 es: {lista1}')
print(f'La lista 2 es: {lista2}')

print('Los elementos que se extrajeron de la lista 1 son: ')
print(comparar_listas(lista1, lista2))

print('La lista filtrada sin los elementos repetidos en ambas listas es: ')
print(array_diff(lista1, lista2))
