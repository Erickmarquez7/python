"""Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos 
de cada uno"""

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio

class Moto(Fabrica):
    def get_datos(self):
        print('La moto tiene {} llantas'.format(self.llantas))
        print('La moto es de color', self.color)
        print('La moto cuesta $', self.precio)

class Carro(Fabrica):
    def get_datos(self):
        print('El carro tiene {} llantas'.format(self.llantas))
        print('El carro es de color', self.color)
        print('El carro cuesta $', self.precio)

moto = Moto(2, 'azul', 10000)
carro = Carro(4, 'verde', 10)

moto.get_datos()
carro.get_datos()

print(type(moto))
print(type(carro))
