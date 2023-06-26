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