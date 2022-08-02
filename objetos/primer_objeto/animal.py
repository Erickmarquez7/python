class Animal:
    #variable de clase, es como static en java
    x = 0

    def grupo(self):
        #debemos de poner self para que entienda que es la varibale del mismo
        self.x = self.x+1
        print('Hasta ahora: ', self.x)

    def metodo():
        #Este método no funciona jsjs
        print('ah caray')

an = Animal()
#el argumento se llama automaticamente
an.grupo()
an.grupo()
an.grupo()
#De hecho es como si hiciera esto, lo mismo que en el archivo lista.py
#Me recuerda un poco a calculo lambda, lol
Animal.grupo(an)
#Estás obligado a poner el self, ya que py le pasa el argumento self
#an.metodo()