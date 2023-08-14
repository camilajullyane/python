                                #   JOKENPO CONTRA O COMPUTADOR
from random import randint
from random import choice
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
#print(f'O computador escolheu {itens[computador]}')


print('-=' *30)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))
#print(f'Você escolheu {itens[jogada]}')

print('JO')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')

if jogada == 0 and computador == 0 or jogada == 1 and computador == 1 or jogada == 2 and computador == 2:
    print(f'EMPATE! O computador jogou {itens[computador]} e você jogou {itens[jogada]}')
elif jogada == 0 and computador == 2 or jogada == 2 and computador == 1 or jogada == 1 and computador == 0:
    print(f'Você VENCEU! PARABÉNS!!. O computador jogou {itens[computador]} e você jogou {itens[jogada]}.')
else:
    print(f'Você PERDEU!!. O computador jogou {itens[computador]} e você jogou {itens[jogada]}.')
    