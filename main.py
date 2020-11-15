import barajaC


palos = ['o','c','e','b']
numeros = ['A','2','3','4','5','6','7','S','C','R']

miB = barajaC.Baraja(palos, numeros)

print(miB.mazacote)
print(miB.repartir(3,5))

miB.barajar()
print(miB.mazacote)