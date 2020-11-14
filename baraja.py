import random

def crearBaraja(palos, numeros):
    baraja=[]
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja 

def barajar(lista_cartas):
    for i in range(len(lista_cartas)):
        nueva_pos = random.randrange(len(lista_cartas))
        ''' Intercambio de cartas, tecnica de vaso vacio '''
        aux = lista_cartas[nueva_pos]
        lista_cartas[nueva_pos] = lista_cartas[i]
        lista_cartas[i] = aux
    return lista_cartas

