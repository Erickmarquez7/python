#tupla con los meses del año, pide al usuario un numero, el que haya ingresado 
#es el mes que debe mostrar en la tupla
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

n = int(input('Elige un mes: '))

print(meses[n-1])

# paises y su capital: diccionario
paises = {'Guatemala': 'Ciudad de Guatemala', 
          'El Salvador': 'San Salvador', 
          'Honduras': 'Honduras',
          'Nicaragua': 'Managua', 
          'Costa Rica': 'San Jose', 
          'Panama': 'Panama', 
          'Argentina': 'Buenos Aires', 
          'Colombia': 'Bogota', 
          'Venezuela': 'Caracas', 
          'España': 'Madrid'}

pais = input('Escribe un pais: ')
pais = pais.capitalize()

if pais not in paises:
    print("El pais no se encuentra, F")
else:
    print(paises[pais])

# Las pilas se pueden emular con las listas, 
# las colas se importan con from collections import deque