from random import randint
print('=-' * 20)
print('     VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 20)

cont = 0

while True:
    computador = randint(1, 10)
    usuario = int(input('Diga um valor: '))
    jogada = str(input('Par ou ímpar? [P/I] ')).upper()
    res = computador + usuario
    aux = ''

    if res % 2 == 0:
        aux = 'PAR'
    else:
        aux = 'IMPAR'
    if jogada == aux[0]:
        print('Você GANHOU!!')
        cont += 1
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!!')
        print('=-' * 20)
        print(f'GAME OVER! Você venceu {cont} vez')
        break
print(f'Você jogou {usuario} e o computador jogou {computador}. O total de {res} DEU {aux}')