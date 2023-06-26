"""
Dado un archivo de texto cuenta la frecuencia con que aprece cada caracter
Para ejecutarlo solo es necesario utilizar el interpretador de python

python3 frecuencia.py
"""


def contador(texto, carac):
    """Contador de caracteres en una cadena"""
    cont = 0
    for c in texto:
        if c == carac:
            cont+=1
    return cont

nombre = "texto.txt"

#abrimos el archivo a leer y lo leemos
with open(nombre) as archivo:
    texto = archivo.read()

#Recorremos el abecederio y tomamos su frecuencia en el texto
for c in "abcdefghijklmnopqrstuvwxyz":
    #sacamos el porcentaje
    por = 100 * contador(texto, c) /len(texto)
    #caracter y porcentaje redondeado a 2 
    print('{0} - {1}'.format(c, round(por,2)))

    