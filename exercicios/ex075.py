
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
           
print(num)
print(f'O valor 9 aparaceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado')
print('Os valores que são divisíveis por 2 são: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')