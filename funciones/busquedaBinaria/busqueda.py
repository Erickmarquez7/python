import random
import sys

def arreglo(n):
    """Crea un arreglo de tamaño n rellenado con 0"""
    arreglo = []
    for _ in range(n):
        arreglo.append(0)
    return arreglo


def rellena(arreglo):
    """Rellena el arreglo de tal forma que para toda i, 0 <= i <= n-1, se tiene
    que |A[i] - A[i-1]| <= 1"""
    j =0
    for i in range(len(arreglo)):
        r = bool(random.choice([True, False]))
        if r:
            arreglo[i] = j
        else:
            arreglo[i]=j
            j=j+1
    return arreglo


def busqueda(arreglo, izq, der, z):
    """Funcion de busqueda principal en tiempo log n"""
    mid = ((izq + der)//2)
    if (izq > der or mid >len(arreglo)-1): return -1 #Significa que no lo encontró
    else:
        if arreglo[mid] == z: return mid
        elif z < arreglo[mid]: return busqueda(arreglo, izq, mid-1, z)
        else: return busqueda(arreglo, mid+1, der, z)

#arr = rellena(arreglo(10))
#print(arr)
#arr = [1,4,5,6]
#indice = busqueda(arr, 0, len(arr), 6)
#print(indice)

#--------main xd
n = sys.argv[1]
n = int(n)

print("El arreglo es: ")
arr = rellena(arreglo(n))
print(arr)
z = random.randint(0,n)
print("El numero a buscar es: " + str(z))

print(" El indice del elemento es: "+str(busqueda(arr, 0, len(arr), z)))
