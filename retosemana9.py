# Este programa pide al usuario ingresar una letra dentro de un bucle infinito para luego ejecutar una funcion que muestra
# en pantalla la letra anterior y siguiente dentro del alfabeto.

# 1. Pedir al usuario ingresar una letra
# 2. impromir en pantalla la letra siguiente y anterior en el alfabeto de la letra ingresada
# 3. Finalizarl el programa cuando el usuario ingrese la palabra "Exit"

# Primero de define el diccionario que se utilizara en el programa, en este caso es el diccionario Español

alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

# En este bloque definiremos la funcion que se utilizara en el programa


def muestraletras():
    """
    Esta funcion recibe un caracter cualquiera ingresado por el usuario y dice si pertenece al diccionario,
    En caso de que si pertenezca imprime en pantalla que letra es, cual es la anterior letra en orden alfabetico y cual
    es la siguiente en ese mismo orden. Ademas permite al usuario salir del bucle infinito en cualquier momento escribiendo
    la palabra "salir" """

    for letra in alfabeto:
        letra = input('Por favor ingrese una letra: ').capitalize()
        if letra == 'Salir':
            print('Ha finalizado el programa.')
            exit()
        if letra == 'A':
            print(
                f'A es la primera letra del diccionario y la letra siguiente a A es {alfabeto[1]} ')
            print(finalizar)
        if letra == 'Z':
            print(
                f'Z es la ultima letra del diccionario y la letra anterior a Z es {alfabeto[25]}')
            print(finalizar)
        elif letra in alfabeto:
            i = alfabeto.index(letra)
            print(
                f'la letra escrita es {alfabeto[i]}, la letra anterior es {alfabeto[i - 1]} y la letra siguiente es {alfabeto[i +1]}')
            print(finalizar)
        else:
            print('No ha ingresado una letra')
            break

# En este bloque se definen las variables globales del programa


finalizar = 'Puede salir del programa cuando lo desee escribiendo la palabra "Salir".'

inicio = input(
    'Si desea finalizar el programa escriba la palabra "Salir", de lo contrario escriba cualquier caracter: ').capitalize()

# En este ultimo bloque se establece el bucle infinito al cual estara sujeto el programa

while inicio != 'Salir':
    muestraletras()
if inicio == 'Salir':
    print('Ha finalizado el programa')
    exit()

# Fin del programa
