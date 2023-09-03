lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    escolha = input('Quer continuar? [S/N] ').strip().upper()
    if escolha == 'N':
        print(f'Você digitou os valores {lista}')
        break