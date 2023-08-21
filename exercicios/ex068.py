from random import randint
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]'))
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
