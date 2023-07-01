"""
Crear una clase llamada Marino() con un metodo que sea hablar en donde 
muestre un mensaje que diga "Hola...". Luego
crear una clase Pulpo() que herede Marino pero 
modificar el mensaje de hablar por "Soy un Pulpo". 
Por ultimo crear una clase Foca() heredada de Marino pero 
que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parametro"""

class Marino():
    def saludo(self):
        print('oli crayoli')
        #Ejemplo de las patas del pulpo y como se pasa asi mismo como argumento
        #print(self.patas)

class Pulpo(Marino):
    #python detecta que se trata de polimorfismo
    def saludo(self):
        self.patas = 8
        print('Soy un pulpo')

class Foca(Marino):
    #python detecta que se trata de polimorfismo
    def saludo(self, mensaje):
        #al ponerle self lo crea coo atributo
        self.mensaje= mensaje
        print(self.mensaje)

marino = Marino()
marino.saludo()

pulpo = Pulpo()
pulpo.saludo()

foca = Foca()
foca.saludo('foc foc foc')

Marino.saludo(pulpo)