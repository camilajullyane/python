num = 0
res = 'S'
cont = 0
soma = 0
maior = menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    res = input('Quer continuar? [S/N] ')
    if num > maior:
        maior = num
    else:
        menor = num
    if res in 'Ss':
        num = int(input('Digite um número: '))
        cont += 1
        soma += num
        res = input('Quer continuar? [S/N] ')
        if num > maior:
            maior = num
        else:
            menor = num

print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
