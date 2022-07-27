class Punto:
    #recordemos que es diferente variables de clase a variables de instancia
    '''Representación de puntos en coordenadas rectangulares'''

    def __init__(self, x, y):
        #definimos el "constructor"
        '''#definimos constructor
        Recibe como primer parametro la instancia sobre la cual
        está trabajando, esto aplica para todos los metodos de la clase
        es equivalente o parecido a decir algo como
        __init__(Punto, x, y)'''
        self.x = x
        self.y = y

p = Punto(3,7)
print(p) #tenemos que definir su forma de imprimir, sino solo nos dirá la memoria
print(p.x)
