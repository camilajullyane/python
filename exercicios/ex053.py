frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)

print(f'O inverso de {frase} é {frase[::-1]}')

if frase == frase[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')