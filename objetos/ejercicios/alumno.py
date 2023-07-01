"""Realizar un programa que conste de una clase llamada Alumno 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Alumno():
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def get_datos(self):
        print('nombre: {}'.format(self.nombre))
        print('nota: {}'.format(self.nota))

    def pasa(self):
        if self.nota < 6:
            print('No pasa, no pasa')
        else:
            print('Si pasa')

alumno1 = Alumno()
#Si comentamos la linea entonces va a tener un AtributteError en get_error
alumno1.datos('Erick', 10)
alumno1.get_datos()
Alumno.pasa(alumno1)