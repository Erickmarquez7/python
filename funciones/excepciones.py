"""Cachando excepciones con try catch"""


def try_catch():
    while(True):
        try:
            var = int(input("Introduce un numero: "))
            x = 5
            print('El resultado de la multipliación es', var*x)
        #break
        except:
            print('Ingresaste otra cosa, intenta de nuevo')
        #se ejecuta si logra hacer el try
        else:
            print('mensaje del else')
        finally:
            print('Este mensaje siempre aparece')

#try_catch()


def multiples():
    try:
        var = int(input('Escribe lo que sea: '))
        print(10//var)
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    except ValueError:
        print('Debe ser un numero, papito')
    #Para saber mas acerca de la excepcion
    except Exception as x:
        print(x)
        print(type(x))
        print(type(x).__name__)

#multiples()
#Podemos utilizar raise para mandar excepciones