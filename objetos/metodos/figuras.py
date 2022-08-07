class Figura:
    def __init__(self, nombre):
        '''asgina nombre a la figura'''
        self.nombre = nombre
    
    def prints(self):
        print(self.nombre)
        #imprime su nombre, recordemos que es como si le pasaras el mismo como argumento
        #y se pasa implicitamente
    
    # def printn(self):
    #     print(nombre)

cuadrado = Figura('cuadrado')
triangulo = Figura('triangulo')
circulo = Figura('circulo')

cuadrado.prints()
#c = cuadrado.nombre
#print(c) da lo mismo. No tenemos encapsulacion de atributos... Por ahora

p = circulo.prints #si ponemos los () se manda a llamar el metodo, por lo cual imprime el nombre
#pero si lo dejamos así tenemos que poner a 'p' con () para que se imprima el nombre

#Recordemos el uso del self
Figura.prints(triangulo) #Como si metodo de clase en Java xd
triangulo.prints()#De instancia

rombo = Figura('rombo')
rombo.prints()
Figura.prints(rombo)
Figura.prints(circulo)



#Y si le paso otra instancia no perteneciente a la clase?
class Forma:
    def __init__(self, nombre):
        self.nombre= nombre

    def pri(self):
        print(self.nombre)

estrella = Forma('estrella')
estrella.pri()
Forma.pri(estrella)

luna = Forma('luna')
luna.pri()

##Pasamos diferente instancia a la clase
#Imprime luna, pues la clase toma el argumento y es el argumento a quien le pedimos que imprima
#en la linea 7
Figura.prints(luna)

Forma.pri(estrella)
#Imprimirá cuadrado por la misma razon
Forma.pri(cuadrado)

print(type(Forma)) #Si ponemos tipo es diferente tanto en clase como instancia
print(type(luna))