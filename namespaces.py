# Probando ambitos

titulo = 'Probando ambitos'
suma = 10.5


def sumar():
    suma = 2 + 2
    titulo = titulo + 'mundo'  # Error porque no esta definida en el ambito local
    print(titulo)
    print('Suma ambito local', suma, id(suma))


print('Antes de llamar a la funcion')
print('Suma en ambito global', suma, id(suma))
sumar()
print('Despues de llamar a la funcion sumar')
print('Suma en ambito global', suma, id(suma))
