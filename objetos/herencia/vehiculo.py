#Empecemos con el ejemplo mas comun xd
class Vehiculo:
    def __init__(self, color):
        self.color = color
        self.prendido = False

    def enciende(self):
        self.prendido = True

    def apaga(self):
        self.prendido = False

    #def __str__(self):
    #    return ('Clase padre ', self.color)


#Podria ser que vehiculo sea abstracto pero no nos adelantemos


#Ponemos entre () a la clase eque extiende
class Carro(Vehiculo):

    def __init__(self, color):
        super().__init__(color)
        self.llantas = 4
    
    def sonido(self):
        print('Ruuuuuuuuun xd')

    def comprueba(self):
        print('Comprobacion:', self.color)
        if self.prendido:
            print('Vehiculo disponinle')
        else:
            print('Apagado')
        
        print('No llantas:', self.llantas)
        print('----------')

    #def __str__(self):
    #    return 'Clase hija jsjs'


carro = Carro('azul')
carro.comprueba()
carro.enciende()
carro.comprueba()

#Lo creamos con clase padre
carro2 = Vehiculo('Verde')
#carro2.comprueba() #No jala porque Vehiculo no tiene el metodo 'comprueba'
carro2.enciende() #en java si jalaria
#carro2.comprueba()
#Entonces veamos de que tipo son cada uno


print(type(carro))
#<class '__main__.Carro'>

print(type(carro2)) 
#<class '__main__.Vehiculo'>
#Así ya tiene mas sentido xd