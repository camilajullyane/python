
soma = 0
qtd = 0
menor = 0
cont = 0
barato = ' '

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if preco > 1000:
        qtd += 1    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).upper()[0].strip()
    
    if escolha == 'N':
        print('FIM DO PROGRAMA')
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {qtd} iten(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato}')