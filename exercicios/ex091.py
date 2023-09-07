from random import randint
from time import sleep

jogadores = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)

}

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

jogadores_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True)) #ordena o dicionário de forma decrescente
print('='*30)
print('RANKING DOS JOGADORES')
print('='*30)
cont = 1
for k, v in jogadores_ordenado.items():
    print(f'{cont} lugar: {k} com {v}')
    cont += 1