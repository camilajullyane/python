maioridade = 0
sexo_masculino = 0
sexo_feminino = 0
escolha = ' '
sexo = ' '
while True:
    print('-=' *20)
    print('CADASTRE UMA PESSOA')

    idade = int(input('Idade: '))
    
    sexo = str(input('Sexo:[M/F] ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()

    escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()

    print('-='*20)
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        sexo_masculino += 1
    if sexo == 'F' and idade < 20:
        sexo_feminino += 1
    if escolha == 'N':
        break
print(f'{sexo_masculino} homens foram cadastrados')
print(f'{maioridade} pessoa(s) tem acima de 18 anos')
print(f'{sexo_feminino} mulher(es) tem abaixo de 20 anos')    