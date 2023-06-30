"""Crear un programa que tenga una lista, 
luego crear una funcion con la cual se van a pedir numeros al usuario 
para agregar a la lista. Debes crear una segunda funcion en donde se 
ordenen los numeros pares e impares dentro de dos listas nuevas"""
lista = [1,2,3,4,5]

def pide():
    entrada = int(input('Escribe el numero deseas ingresas a la lista: '))
    lista.append(entrada)

def ordena():
    lista.sort()
    par = []
    inpar = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            inpar.append(i)
    return par, inpar


pide()
x, y = ordena()
print(x)
print(y)