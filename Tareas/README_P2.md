Para entender con mayor facilidad los dos programas del proyecto, se dividiran en dos partes
La primera parte contendra el programa para identificar la longitud de una palabra ingresada, mientras que
la segunda parte contendra el programa que identificara la pertenencia a un cuadrante especifico
de los datos ingresados por el usuario.

En la parte 1 del proyecto realice el programa que verifica la longitud de caracteres que posee una palabra
y la clasifica como correcta si esta entre 4 y 8 caracteres.

1. Utilice un ciclo while para verificar que los datos ingresados por el usuario por medio de input
   fueran correctos y en caso de no serlos pedir que los ingrese nuevamente. Una vez los ingrese correctamente puede continuar con el programa
2. Utilice la funcion len() para establecer la cantidad de caracteres que tiene la palabra ingresada por el usuario.

3. Una vez establecida la longitud, se verifica su longitud y se establece si es:
   correcta: entre 4 y 8 caracteres
   faltan caracteres: menos de 4 caracteres
   sobran caracteres: sobran caracteres

4. Una vez se establece a que grupo de respuesta pertenece se le informa al usuario por medio de un print
   y se finaliza el programa.

En la parte 2 del proyecto realice el programa que verifica a que cuadrante del plano cartesiano pertenecen
los valores asignados a (x,y) por el usuario. Tambien pueden pertenecer a algun eje o al origen.

1. Estableci las variables a utilizar dentro del programa asi como la lista vacia a traves del comando lista = []

2. Estableci un verificador a traves de un ciclo while y de los comandos try y except para verificar
   que los datos ingresados por el usuario fueran numeros enteros.

3. Luego utilice la funcion append() para agregar los valores de x,y a la lista vacia anteriormente creada.

4. En el primer bloque de condicionales estableci como resultados si los valores de (x,y) estaban en el origen o sobre alguno de los ejes x o y, si lo estaba, se le informaba al usuario y se finalizaba el programa.

5. En caso de que no estuvieran en alguno de ellos se le informaba al usuario que los datos (x,y) pertenecen a alguno de los cuadrantes.

6. Si los datos pertenecian a algun cuadrante, en el siguiente bloque de condicionales se establecia a cual de ellos pertenecia.

7. Una vez se obtuviera el resultado se le informa al usuario mediante un print a cual de los cuadrantes pertenece los datos que ha ingresado. Y de esta forma finaliza el programa.

Feedback del modulo:
