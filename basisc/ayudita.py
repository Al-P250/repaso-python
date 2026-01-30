def printMatrix(matriz):
    for fila in matriz:
        print(fila)









"""1. Dibujar una matriz cuadrada con el tamaño definido por el usuario y que pinte de unos la diagonal inversa.

2. Llenar una matriz cuadrada (4x4) de números aleatorios del 0 al 9 y mostrar la suma de sus filas y sus columnas.

3. Comprobar si una matriz dada es un cuadrado mágico.
cuadradoMágico = [[16,3,2,13], [5,10,11,8], [9,6,7,12], [4,15,14,1]] 

4. Realiza un programa de cambio de divisas euro-latam. Almacenaremos en una tabla los cambios respecto al euro. La idea es que una
vez el usuario introduzca una cantidad de euros y la moneda a la que quiere cambiar, y le devuelva la cantidad cambiada.

Bolívar Venezolano - 202,78
Guaraní Paraguayo - 8.336,03
Peso Argentino - 1.564,31
Peso Boliviano - 8,0736
Peso Chileno - 1.120,74
Peso Colombiano - 4.562,79
Peso Uruguayo - 46,602
Real Brasileño - 6,2661
Sol Peruano - PEN - 4,0908

5. Programa un juego de búsqueda de un tesoro. Contaremos con una matriz de 4x5, tendremos un tesoro y una mina. El juego termina cuando 
pisas la mina (pierdes) o cuando encuentras el tesoro (ganas). El menú de juego tendrá el siguiente aspecto:

¡Busca el tesoro!
3|
2| 
1|
0|
  ----------
   0 1 2 3 4 

Coordenada x: (input del usuario, p.e. 3)
Coordenada y: (input, p.e. 1)

3|
2| 
1|       X
0|       
  ----------
   0 1 2 3 4 
   
Coordenada x: (input del usuario, p.e. 2)
Coordenada y: (input, p.e. 0)

3|
2| 
1|       X
0| X      
  ----------
   0 1 2 3 4 

Coordenada x: (input del usuario, p.e. 2)
Coordenada y: (input, p.e. 2)

¡Enhorabuena, has encontrado el tesoro!
3|
2|     €
1|       X
0| X   *        <-- Aquí estaba la mina. Programar también cuando pierdes.
  ----------
   0 1 2 3 4 
   
   
6. Ahora, mejora el juego y avisa al usuario cuando marque si tiene una mina a una casilla de distancia. """