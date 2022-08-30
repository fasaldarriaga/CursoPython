# Solicitar cierto numero de personas
# 1. solicite el nombre de cada persona
# 2. Pregunte la edad de cada persona
# 3. Pregunte el sexo
# Si no especifica el ssexo, guarda la variable como 'No especificada'
# Se unen los tres datos introducidos

def agregar_datos(lista, valor):
    """
    Funcion que agrega un dato a una lista especificada
    """
    if valor == ' ':
        valor = 'No especificado'
    lista.append(valor)
    return lista


nombres = []
edades = []
sexos = []

personas = int(input('Cuantas personas desea resgitrar?: '))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i + 1}: ').title()
    nombres = agregar_datos(nombres, nombre)
for i in range(personas):
    edad = input(f'Ingrese la edad de {nombres[i]}: ')
    edades = agregar_datos(edades, edad)
for i in range(personas):
    sexo = input(f'Cual es el sexo de {nombres[i]}: ')
    sexos = agregar_datos(sexos, sexo)

for i in zip(nombres, edades, sexos):
    print(i)
