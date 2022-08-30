def sumar(parametro1, parametro2):
    """Funcion que suma dos parametros y los muestra en pantalla"""
    print('Suma:', parametro1 + parametro2)


argumento1 = 5
argumento2 = 7

# Invocando a la funcion por medio de parametro variables
sumar(argumento1, argumento2)

# Invocando a la funcion por medio de parametros de valor
sumar('mundo!', 'Hola')
sumar('Hola ', 'mundo!')  # Hay que respetar el orden de los parametros

# Error porque la funcion esta definida para dos parametros y debe respetarse esa definicion
sumar('hola')

################################################################

# Parametros opcionales


def muestra_alumno(nombre, edad=18, sexo='f'):
    """ ES una funcion que muestra en pantalla el nombre, edad y sexo de un alumno
    Recibe 3 parametros
    1. nombre
    2. edad = 18
    3. Sexo = f 
    """
    print(f'Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}')


# Ejecucion de funcion con parametro obligatorio
muestra_alumno('Maria')

# Ejecucion utilizando el parametro obligatorio y uno opcional
muestra_alumno('Maria', 22)

# Ejecucion de funcion con el primer y ultimo parametro
muestra_alumno('Juan', sexo='M')
