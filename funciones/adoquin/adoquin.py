#importamos math para las potencias, time para que se muestre mejor paso a paso
#random para poner el cuadrado al azar, numpy pa que nos facilite la bida
#sys para los argumentos 
from math import log, floor
from time import sleep
import random
import numpy as np
import sys


def comprueba(n):
    '''Dado un numero comprueba si es potencia de dos'''
    if n < 1:
        return False
    i = log(n, 2)
    return 0 == (i - floor(i))


def imprime_bonito(arreglo):
    '''Dado un arreglo de nxn imprime cada renglón para que se vea legible'''
    for i in range(len(arreglo)):
        print("[" + ','.join(arreglo[i]) + "]")



def adoquin(n):
    '''Comprobamos que sea potencia de dos,
        si lo es mandamos a llamar el algoritmo recursivo'''
    if not comprueba(n):
        print('No es potencia de dos, no se puede')
        return ""
    else:
        cuadri = [[' '] * n for i in range(n)]
        i = random.randint(0,n-1)
        j= random.randint(0,n-1)
        cuadri[i][j]= 'a'
        #n la pasamos para hacer recursion sobre ella
        cuadri = np.array(cuadri)
        #print(cuadri)
        print("La cuadricula con el cuadrado especial 'a' es: ")
        imprime_bonito(cuadri)
        print("Ejecución del algoritmo")
        adoquin_main(cuadri)

#adoquin(4)

def busca_a(cuadri):
    '''Encuentra la posición de a empezando desde 1 para facilitar un poco el calculo xd en cuadrante'''
    #solo lo usamos para que sea mas facil encontrar el cuadrante
    np_array=np.array(cuadri)
    i, j = np.where(np_array =='a')
    i = int(i)+1
    j = int(j)+1
    return i, j


def cuadrante_f(cuadri):
    '''Nos dice en que cuadrante esta el adoquin'''
    i, j = busca_a(cuadri)
    n = len(cuadri)//2
    if i<=n and j<=n: 
        return 1
    if i<=n and j>n: 
        return 2
    if i>n and j<=n: 
        return 3
    else: 
        return 4


def adoquin_main(cuadri):
    #caso base de 1, el adoquin ya esta
    #tamano es par
    tamano = len(cuadri)
    if tamano == 1: 
        #print("n=1")
        return cuadri
    if tamano == 2:       #  [a, ]
        #caso donde            , ], así rellenamos los demas espacios con el adoquin
        print("donde se encuentra la a en el caso base")
        imprime_bonito(cuadri)
        print("Completando el caso base")
        if cuadri[0][0] == 'a': 
            #print("Inicio del caso base en el cuadrante 1")
            cuadri[0][1] = 'a'
            cuadri[1][0] = 'a'
            cuadri[1][1] = 'a'            
            imprime_bonito(cuadri)
            print("")

          #  print("Fin del caso base en el cuadrante 1")
        # [[ ,a],
        #  [ , ]]
        elif cuadri[0][1] == 'a': 
           # print("Inicio del caso base en el cuadrante 2")
            cuadri[0][0] = 'a'
            cuadri[1][0] = 'a'
            cuadri[1][1] = 'a'
            imprime_bonito(cuadri)
            print("")
            #print("Fin del caso base en el cuadrante 2")


        # [[ , ],
        #  [a, ]]
        elif cuadri[1][0] == 'a': 
            #print("Inicio del caso base en el cuadrante 3")
            #coloreamos los demás
            cuadri[0][1] = 'a'
            cuadri[0][0] = 'a'
            cuadri[1][1] = 'a'
            imprime_bonito(cuadri)
            print("")
            #print("Fin del caso base en el cuadrante 3")

        
        # [[ , ],
        #  [ ,a]]
        else:
            #print("Inicio del caso base en el cuadrante 4")
            cuadri[0][1] = 'a'
            cuadri[1][0] = 'a'
            cuadri[0][0] = 'a'
            imprime_bonito(cuadri)
            print("")
            #print("Fin del caso base en el cuadrante 4")

        sleep(1.5)

    #el caso recursivo en los catro cuadramtes, me dio amsiedad
    else:
        #print("caso rec")
        #sacamos en cual cadrante esta el adoquin
        cuadrante = cuadrante_f(cuadri)
        #notemos que pos es un numero par
        pos = tamano//2
        #rellenamos el cuadrante con el adoquin y luego mandamos a llamar de manera rec
        #print("rellena")
        if cuadrante == 1:
            #print("cuadrante 1")
            cuadri[pos][pos] = 'a' 
            cuadri[pos-1][pos] = 'a' 
            cuadri[pos][pos-1] = 'a'
            imprime_bonito(cuadri)

        if cuadrante == 2:
            #print("cuadrante 2")
            cuadri[pos][pos] = 'a' 
            cuadri[pos-1][pos-1] = 'a'
            cuadri[pos][pos-1] = 'a' 
            imprime_bonito(cuadri)

        if cuadrante == 3:
            #print("cuadrante 3")
            cuadri[pos][pos] = 'a' 
            cuadri[pos-1][pos-1] = 'a'
            cuadri[pos-1][pos] = 'a' 
            imprime_bonito(cuadri)

        if cuadrante == 4: 
            cuadri[pos][pos-1] = 'a' 
            cuadri[pos-1][pos] = 'a' 
            cuadri[pos-1][pos-1] = 'a'
            imprime_bonito(cuadri)
            #print("cuadrante4")

        #mandamos a llamar rec en los cuatro cuadrantes
        cuadri1 = cuadri[0: pos, 0: pos]
        cuadri2 = cuadri[0:pos, pos: tamano+1]
        cuadri3 = cuadri[pos: tamano+1, 0: pos]
        cuadri4 = cuadri[pos: tamano+1, pos:tamano+1]
        sleep(1.5)
        print(" +Inicio del caso recursivo en el cuadrante 1")
        adoquin_main(cuadri1)
        imprime_bonito(cuadri)
        print(" -Fin del caso recursivo en el cuadrante 1")
        sleep(1.5)
        print(" +Inicio del caso recursivo en el cuadrante 2")
        adoquin_main(cuadri2)
        imprime_bonito(cuadri)
        print(" -Fin del caso recursivo en el cuadrante 2")
        sleep(1.5)
        print(" +Inicio del caso recursivo en el cuadrante 3")
        adoquin_main(cuadri3)
        imprime_bonito(cuadri)
        print(" -Fin del caso recursivo en el cuadrante 3")
        sleep(1.5)
        print(" +Inicio del caso recursivo en el cuadrante 4")
        adoquin_main(cuadri4)
        imprime_bonito(cuadri)
        print(" -Fin del caso recursivo en el cuadrante 4")
        sleep(1.5)
    #imprime_bonito(cuadri)

#prueba de n=2
prueba2 = [[' ', 'a'], 
           [' ', ' ']]


#prueba de n=4
prueba4 = [[' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', 'a', ' ', ' ']]


prueba8 = [[' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ','a',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '],
           [' ',' ',' ',' ',' ',' ',' ', ' '] ]


#adoquin(8), modificar esta linea si queremos porbar alguno de los 3 ejemplos de arriba

n = sys.argv[1]
n = int(n)
adoquin(n)