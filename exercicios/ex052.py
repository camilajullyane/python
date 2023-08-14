                        # DETECTOR DE NÚMEROS PRIMOS

num = int(input('Digite um número: '))

cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[31m{c}\033[m', end = ' ')
        cont += 1
    else:
        print(f'\033[32m{c}\033[m', end = ' ')
    
print(f'\nO número {num} foi divisível {cont} vezes')
if cont > 2:
   print('E por isso ele NÃO É PRIMO!!')
else:
    print('E por isso ele É PRIMO!')

