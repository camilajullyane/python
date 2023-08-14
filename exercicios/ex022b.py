                         #Analisador de textos

nome = str(input('Nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome maiúsculo é:  {nome.upper()}')
print(f'Seu nome minúsculo é: {nome.lower()}')
print('Seu nome tem {}'.format(len(nome) - nome.count(' ')))
nome_div = nome.split()
print(f'Seu primeiro nome tem {len(nome_div[0])} letras') 

