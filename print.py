# funcion print
# print("hola", 9 , "Hello") # Se pueden imprimir varios valores sin importar si no son de las mismas caracteristicas
# print(" El resultado de 1 + 2 es: " , 3)

# Ejemplos de cadenas formateadas
# print("El numero 15 en sistema decimal es %d, en sistema octal es %o, en el sistema hexadecimal es %x," % (15, 15, 15))
# pi = 3.14192
# r = 5
# print(
#     f"El radio de un circulo es (r) y el area de un circulo es {pi* r**2: .2f}")

# Impresion de caracteres especiales
# print("La letra beta es:\n\t \u03b2 ") # \n: espacio , \t: tabulacion (4 por defecto) \u03b2: Representacion de beta en sistema "asis"

# Caracteres de escape
from re import T


print("Halo world", end=" ")  # Se pone un espacio en vez de un salto de linea
print("Otra vez", end="\t")
print("Y otra vez")
