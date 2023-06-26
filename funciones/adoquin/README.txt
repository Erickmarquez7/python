Para la correcta ejecución del programa es necesario tener instalada la biblioteca numpy de python ya que con esta trabajamos a las subcuadriculas al partirlas

Dependerá de cada sistema operativo el cómo instalarlo

Una vez que lo tengamos instalado podemos correr el programa con

python main.py <n>

Donde n es el tamaño de la cuadricula, el cual debe ser un entero no negativo potencia de dos

Para poder entender mejor el algoritmo dividimos la cuadricula por cuadrantes, donde cada cuadrante es 
 ___________
|     |     |
|  1  |  2  |
|_____|_____|  
|     |     |
|  3  |  4  |
|_____|_____|

Y hacemos recursión en cada cuadrante

Cada adoquín se representa con la letra 'a', el primer adoquín se mostrará en la terminal de manera al azar dentro de la cuadricula, luego se irá mostrando cómo se va rellenando adoquín dentro del cuadrante de manera recursiva