lista = []
par = []
impar = []

while True:
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    res = input('Quer continuar? [S/N] ').upper()
    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').upper()

    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)
    if res == 'N':
        print(f'A lista completa é: {lista}')
        print(f'A lista de pares é: {par}')
        print(f'A lista de ímpares: {impar}')
        break
   
