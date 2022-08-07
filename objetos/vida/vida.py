class Planeta:
    ult=''

    def __init__(self, nombre):
        self.nombre = nombre
        self.ult = nombre #el ultimo que se construyo
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