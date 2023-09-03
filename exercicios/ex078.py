'''lista = []
maior = menor = 0
for j in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {j}: ')))
    if j == 0:
        maior = menor = lista[j]
    else:
        if lista[j] > maior:
            maior = lista[j]
        if lista[j] < menor:
            menor = lista[j]

print(f'Você digitou os valores: {lista}')
print(f'O maior número foi {maior} nas posições ', end='')
      
for i, v in enumerate(lista):
    if v == maior:
       print(f'{i}... ', end='')
print()
print(f'O menor número foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()

'''

lista = []
for c in range(5):
    lista.append(int(input('Digite um valor: ')))


print(f'\nO maior valor da lista foi {max(lista)} nas posições', end=' ')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f'{c}', end=' ')


print(f'\nO menor valor da lista foi {min(lista)} nas posições ', end=' ')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'{c}', end=' ')