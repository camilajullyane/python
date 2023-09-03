lista = []
res = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuar? [S/N] ').upper()
    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').upper()
    if res in 'N':
        break

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')

print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')