pessoas = []
dados = []
cont = 0
maior = menor = 0

while True:
    dados.append(str(input('Nome: '))) 
    dados.append(float(input('Peso: ')))    
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper()
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta in 'N':
        break

print(f'Foram cadastradas {cont} pessoas')

for c, v in enumerate(pessoas):
    if c == 0:
        maior = menor = v[1]
    if menor > v[1]:
        menor = v[1]
        
    if maior < v[1]:
        maior = v[1]

print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for c, v in enumerate(pessoas):
    if v[1] == maior:
        print(f'{v[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for c, v in enumerate(pessoas):
        if v[1] == menor:
            print(f'{v[0]}')

