# Utilizar al menos 2 funciones
# Preguntar cuantos alumnos se registraran, en caso de no ingresar cantidad, se asume que se registran 3 alumnos
# Preguntara el nombre y 2 calificaciones
# Mostrar el nombre en pantalla con inicial mayuscula y promedio
# Al finalizar el programa se mostrara una lista con el nombre de cada alumno y sus calificaciones

def captura_alumnos(numero=3):
    """
    Registra alumnos y dos calificaciones
    Recibe como parametro la cantidad de alumnos a registrar
    Si no se especifica el numero de alumnos, se registran 3
    """

    lista_alumnos = []
    for i in range(numero):
        nombre = input(f'{i + 1}. Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(
            input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(
            input(f'Ingrese la segunda calificacion de {nombre}: '))
        lista_alumnos.append({nombre, calificacion1, calificacion2})
        promedio(nombre, calificacion1, calificacion2)
    print(lista_alumnos)


def promedio(nombre, calificacion1, calificacion2):
    """
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parametros el nombre y dos calificaciones del alumno
    """

    promedio = (calificacion1 + calificacion2) / 2
    print(f'El promedio de {nombre} es: {promedio}')


numero_alumnos = input('¿Cuantos alumnos desea registrar? ')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
