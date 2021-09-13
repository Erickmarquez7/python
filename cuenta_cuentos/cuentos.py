# !/ cuentos.py
# encoding: latin1

#Está en inglés porque es más fácil conjugar verbos, y poner lugares
import random

#listas de posibilidades, plural
acciones = ['play', 'run', 'read', 'jump', 'fly', 'cut', 'see']
lugares = ['beach', 'hotel', 'forest', 'house', 'plane', 'park']
personas = ['Juan', 'Pepe', 'him', 'her', 'the witch', 'the man', 'the woman', 'it']
sustantivos = ['game', 'book', 'glasses', 'scissor', 'bed', 'rope']

#elige al azar un elemento de las posibilidades, singular
#Son funciones ya que esperamos uno nuevo elemento cada vez que se mande a llamar
def accion():
    return random.choice(acciones)

def lugar():
    return random.choice(lugares)

def persona():
    return random.choice(personas)

def sustantivo():
    return random.choice(sustantivos)


cadena = f'One day our brave character "{persona()}" emerged on an adventure with not much sense, \
his actions seemed to be guided by something "supernatural".\n\
This character was quietly in a {lugar()} doing nothing, literally. \
Suddenly "{persona()}" came to tell him that he had a very important mission, \
there is no time for explanations, he had to {accion()} an {sustantivo()} instead in order to \
release his sins, otherwise at the end of his life he would go where there is no one: {lugar()}.\n\
Immediately he paid attention to him, because he did not want to be in that place, he had to travel \
land, sea and {lugar()} to achive his goal, even on the way he found a new friend: "{persona()}", \
who told him a shortcut to get even faster, he continued his advice.\n\
When he arrived at the {lugar()}, he had to {accion()} the {sustantivo()} that the "{persona()}" had told him, \
but when he did not follow the rules of the game, at the end of his life he went to the {lugar()}'

print(cadena)
