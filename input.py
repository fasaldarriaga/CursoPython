# sirve para capturar datos ingresados por el usuario sin necesidad de definirlos previamente en el codigo
nombre = input("¿Como te llamas? ")
print("Hola " + nombre)

edad = input("¿Que edad tienes? ")
print(type(edad))
print(f'{nombre} tiene {edad} años')

# Programa que pide dos numeros al usuario y los suma
# Hay que tener cuidado con el tipo de datos que se pide, int o el que sea
numero1 = int(input("Introduce un numero: "))
numero2 = int(input('ingrese un segundo numero: '))
numero3 = numero1 + numero2
print(f'El resultado de la suma es:{numero3} ')
