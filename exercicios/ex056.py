media = 0
m = 0
h = ''
maior = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    media += idade/4
    if sexo == 'M':
        if idade > maior:
            maior = idade
            h = nome
    if sexo == 'F' and idade < 20:
        m += 1
print(f'A média de idade do grupo é: {media:.1f}')
print(f'O nome do homem mais velho se chama {h} e ele tem {maior} anos')
print(f'O númeoro de mulheres menores de 20 anos é: {m}')