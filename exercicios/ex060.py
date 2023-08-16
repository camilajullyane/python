n = int(input('Digite um número: '))
cont = n
fat = 1
while cont > 0:
    print(f'{cont}', end= '')
    print(' x ' if cont > 1 else ' = ', end= '')
    fat *= cont
    cont -= 1
print(fat)



'''USANDO BIBLIOTECA MATH

from math import factorial
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'O fatorial de {n} é {fat}')'''