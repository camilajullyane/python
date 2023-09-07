aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] < 7:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'

print(aluno)
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situação"]}')