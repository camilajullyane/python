todos = []
soma = 0

while True:
    pessoa = {}
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma += idade
    sexo = str(input('Sexo: ')).upper()
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    todos.append(pessoa.copy())
    pessoa.clear()
    perg = input('Quer continuar? [S/N] ').upper()
    if perg == 'N':
        break
media = soma / len(todos)
print(f'Foram cadastradas {len(todos)} pessoas')
print(f'A média de idade do grupo é de {media} anos')

print('As mulheres do grupo foram: ', end=' ')
for c in todos:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('As pessoas com idade acima da média foram: ', end=' ')
for c in todos:
    if c['idade'] > media:
        print(c['nome'], end=' ')
