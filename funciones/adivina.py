import random

"""
El usuario adivina el numero al azar producido por la computadora
La computadora genera un numero al azar en un rango determinado por el usuario, 
el objetivo es adivinar dicho numero
Para ejecutarlo solo es necesario utilizar el interpretador de python

python3 adivina.py
"""


def adivina(x):
    """Función principal que genera un numero al azar para que el usario
    adivine dicho numero"""
    azar = random.randint(1, x)
    usuario = 0

    #Así en la primera vuelta nunca va a salir, pues 0 != (1,x)
    while azar != usuario:
        usuario = int(input(f'Adivina el numero entre 0 y {x}: '))
        if usuario > azar:
            print('Número alto, intenta otra vez: ')
        elif usuario < azar:
            print('Número bajo, intenta otra vez: ')
    
    print('Felicidades, acertaste el número')


n = int(input('Ingresa un rango para adivinar un número: '))
adivina(n)