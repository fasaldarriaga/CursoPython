# variables Cast

numero = "147"
print(numero)
print(type(numero))

# convertir la variable de tipo "str" a una variable de tipo "int", "complex",

numero = int(numero)
print(numero)
print(type(numero))

numero = float(numero)
print(numero)
print(type(numero))

numero = complex(numero)
print(numero)
print(type(numero))

# marcara error ya que "una letra no puede convertirse en un valor de tipo int"

# numero = "b"
# numero = int(numero)


bandera = 0
print(bandera)
print(type(bandera))
bandera = bool(bandera)
print(bandera)
print(type(bandera))

# se puede nombrar una variable con:

# "_numero" Pero por buenas practicas se reserva el "_" para distinguir palabras dentro de una variable
# No usar palabras reservadas como: "true, false, print, etc..."
# Las variables son sensitivas a las Mayusculas y minusculas
# x = 7
# print(X) ---> marcara error "X debe ser minuscula = x"

# No se suelen utilizar mayusculas al nombrar variables
#
