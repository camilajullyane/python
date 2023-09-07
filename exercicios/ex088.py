from random import randint
from time import sleep

def inteiroAleatorio(qtd, comeco, fim):
    for c in range(qtd):
        num = randint(comeco, fim)
        if num in jogos[linha]:
            num = randint(comeco, fim)
        else:
            return num


def mostrarJogos():
    print('-' * 20)
    print('JOGA NA MEGA SENA')
    print('-' * 20)


mostrarJogos()
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
print(f'SORTEANDO {qtd} JOGOS' )


for linha in range(qtd):
    jogos.append([])
    for coluna in range(6):
        jogos[linha].append(inteiroAleatorio(qtd, 1, 60))

for c, v in enumerate(jogos):
    print(f'Jogo {c+1}: {v}')
    sleep(1)

