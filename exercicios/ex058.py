from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

computador = choice(lista)
print(computador)
res = int(input('Digite um número de 0 a 10: '))
cont = 0
while res != computador:
    res = int(input('Digite um novo valor de 0 a 10: '))
    cont += 1
print(f'Parabéns! Você adivinhou, o computador pensou no número {computador} e você teve {cont} palpites')