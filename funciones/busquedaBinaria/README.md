El programa recibe un numero natural n y crea una lista con longitud n la cual se rellena al azar con numeros de 0 a n de tal manera que ∀i, 0 ≤ i < n − 1, se tiene que |A[i] − A[i + 1]| ≤ 1 es decir numero con diferencia a lo más 1 no necesariamente distintos.
El programa se ejecuta con

```
python3 main.py n
```

Donde n es el numero natural.
La salida se muestra como

> [0, ..., n-1]

El numero a buscar es z
El indice del elemento buscado es i
El cual z es un numero elegido al azar enrte 0 y n para buscar en el arreglo e i es el indice de z o bien −1 si el elemento no se encuentra.

Notemos que podemos tener listas, de la forma [0, 1, 2, 3, 3, 3, 3, 4, 5, 5] y puede ser el caso que queramos buscar el 3
La busqueda podr ́ıa dar que i = 3 o bien i = 4, i = 5, i = 6, y es correcto pues cumple con la condición de ser igual al elemento buscado.

Por ejemplo, ejecutamos

```
python3 main.py 10
```

Y nos puede dar como salida

> El arreglo es:

> [0, 1, 1, 2, 3, 4, 4, 5, 5, 5]

> El numero a buscar es: 4

> El indice del elemento es: 5

O bien

> El arreglo es:

> [0, 0, 0, 0, 1, 2, 3, 4, 5, 5]

> El numero a buscar es: 7

> El indice del elemento es: -1

Pues recordemos que los elementos del arreglo así como el elemento a buscar z se eligen aleatoriamente.