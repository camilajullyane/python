sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
print(sexo)

while sexo not in 'MmFf':
    sexo = str(input('Informe seu sexo: ').strip().upper())[0]
print(f'Sexo {sexo} registrado com sucesso')