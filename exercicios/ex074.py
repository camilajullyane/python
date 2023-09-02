from random import randint
menor = maior = 0

numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9) )
print(f'Os números sorteados foram: ', end=' ')

for n in numeros:
    print(f'{n}' , end=' ')
    
print(f'O maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')
