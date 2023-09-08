from random import randint
from time import sleep
soma = 0
numeros = []

def sorteia():
    for c in range(1, 6):
        sorteio = randint(1, 6)
        print(sorteio, end=' ', flush=True)
        sleep(0.5)
        numeros.append(sorteio)

def somaPar(lista):
    global soma
    for n in lista:
        if n % 2 == 0:
            soma += n

print('Sorteando 5 valores:')
sorteia()

somaPar(numeros)
print(f'\nSomando os valores pares de {numeros}, temos {soma}')