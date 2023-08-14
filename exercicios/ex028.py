from random import choice
lista = [0, 1, 2, 3, 4, 5]

computador = choice(lista)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

jogador = int(input('Em que número pensei? '))

if jogador == computador:
    print('Você venceu! PARABÉNS!!!!')
else:
    print(f'GAME OVER! Eu pensei no número {computador} e não no {jogador}')

                                                # FAZENDO O PROGRAMA EM LOOP


'''from random import choice
num = [0, 1, 2, 3, 4, 5]

computador = choice(num)

res = int(input('Digite um número de 0 a 5: '))

while True:
    if res == computador:
        print('Você venceu! PARABÉNS!!!!')
        break
    else:
        computador = choice(num)
        res = int(input('Digite um número de 0 a 5: '))'''

    
