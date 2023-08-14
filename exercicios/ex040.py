x = float(input('Primeira nota: '))
y = float(input('Segunda nota: '))
media = (x + y) / 2

if media < 5:
    print('ALUNO REPROVADO')
elif media >= 5 and media <= 6.9:
    print('ALUNO EM RECUPERAÇÃO')
elif media >= 7:
    print('ALUNO APROVADO')