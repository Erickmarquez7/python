"""
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, 
y muestre la siguiente información:

Imprima los dos primeros caracteres.

Imprima los tres últimos caracteres.

Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
"""

var = 'Te quiero solo como amigo' #:(

print(var[0:2])
print(var[-3:])
print(var[::2])
print(var[::-1])
print(var+var[::-1])

"""
En la siguiente lista, debes hacer un programa que muestre los valores al usuario,
a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
"""

lista =  [20, 50, "Curso", 'Python', 3.14]

print(lista)

primero = input("Ingresa el primer elemento: ")
segundo = input("Ingresa el segundo elemento: ")

lista[0] = primero
lista[1] = segundo
