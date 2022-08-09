class Planeta:
    #'''Variables globales'''
    ult=''

    def __init__(self, nombre):
        self.nombre = nombre
        self.ult = nombre #el ultimo que se construyo, pero del objeto
        print(self.nombre, 'construido')

    def total_planetas(self):
        print('Ultimo constriuido:',self.ult)

    #def __del__(self):
        #print(self.nombre, 'a volar')



urano = Planeta('Urano')
neptuno = Planeta('Neptuno')
pluton = Planeta('pluton')

#urano = 1

urano.total_planetas()

#Para hacer static lo hacemos de la siguiente manera
class Animal:
    #Ponemos un contador para simular el static así como el ultimo
    contador = 0

    def __init__(self, especie):
        self.especie = especie
        #Ponemos el nombre de la clase para hacerlo estatico
        Animal.ult = especie
        #De hecho tiene sentido si lo vemos como vemos a self
        Animal.contador = self.contador+1

    def contador_g(self):
        print(Animal.contador)
        print(self.contador)

    def ult_g(self):
        print(Animal.ult)
        print(self.ult)

print('------------------------------')
gato=Animal('gato')
gato.contador_g()
gato.ult_g()

perro = Animal('perro')
perro.contador_g()
perro.ult_g()

mapache = Animal('mapache')
mapache.contador_g()
mapache.ult_g()

#Volvemos con el gato, nos dará el mismo resultado que mapache
#porque son de clase.
gato.contador_g()
gato.ult_g()

#Así que podemos sacarlas como si fuera de clase (porque de hecho así son xd)
(cont, ulti) = Animal.contador, Animal.ult
print(cont)
print(ulti)