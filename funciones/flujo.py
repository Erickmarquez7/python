palabra = 'cadena de prueba'
#Imprimir al revés una cadena
i = len(palabra)-1 
while(i>=0):
    letra = palabra[i]
    print(letra)
    i = i-1
print('-----------------')
#O bien
for letra in palabra:
    print(letra)

#for con listas
lista = ['Postre', 'Comida', 'Bebida', 'Cena']
#Así imprime los elementos de la lista
#ejecuta una vez el cuerpo por cada elemento alimento
#alimento es la variable de iteracion
for alimento in lista:
    print('Esto hay de comer:', alimento)


#print(palabra[:])
#Conjetura de no me acuerdo quien
def conjetura(n):
    valor = int(input('Selecciona un numero: '))
    while (valor != 1):
        print(valor)
        if valor%2 == 0:
            valor = valor//2
        else:
            valor = valor*3+1


mas_comida=['platano', 'queso', 'leche', 'miel']
for alim in mas_comida:
    for letra in alim:
        print(letra)

mas_comida_2=[['agua', 'te', 'cafe'],['huevo', 'arroz', 'chile'],['pan', 'galletas']]


# Dada una letra indica si es vocal o no
# Forma 1
letra = input('1.- Ingresa una letra: ')
if(letra != 'a' and letra != 'e' and letra != 'o' and letra != 'u' and letra != 'i'):
    print('No es vocal')
else:
    print('Es vocal :D')

# Forma 2
letra = input('2.- Ingresa una letra: ')
if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('Es vocal :D')
else:
    print('Nel, no lo es')

# Forma 3 (mas elegante xd)
letra = input('3.- Ingresa una letra: ')
if letra in 'aeiou':
    print('ei, lo es')
else:
    print('Nop, no es')

"""
programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y 
si no, que no riman.
"""
rima1=input('Primera palabra: ')
rima2=input('Segunda palabra: ')

if(len(rima1) < 3 or len(rima2) < 3):
    print("Alguna palabra tiene menos de 3 letras")
elif (rima1[-3:] == rima2[-3:]):
    print('Rima completamente!')
elif (rima1[-2:] == rima2[-2:]):
    print('Rima maso')
else:
    print('nel, no rima')

#Dado un numero al usuario y muestra las tablas de multiplicar de ese numero
num = int(input('Dame un numero: '))
mul = 1
while(mul <= 10):
    res = num * mul
    print('{} x {} = {}'.format(num, mul, res))
    mul=mul+1

# Pide al usuario dos numeros y muestra el rango de numeros entre ambas cifras
numero1 = int(input('Primero numero: '))
numero2 = int(input('Segundo numero: '))

#+1 para incluir al segundo numero
for i in range(numero1, numero2+1):
    print(i)