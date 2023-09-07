def validar(texto):
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        res = str(input(texto)).upper
    return res


alunos = []
dados = []

while True:
    dados.append(input('Nome: '))
    dados.append([float(input('Nota 1: ')), float(input('Nota 2: '))])
    media = (dados[1][0] + dados[1][1]) / 2
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    res = validar('[ERRO DE ENTRADA]. Quer continuar? [S/N] ')
    if res == 'N':
        break
    

print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
for c, v in enumerate(alunos):
    print(f'{c:<4}{v[0]:<10}{v[2]:>8}')

while True:
    pergunta = int(input('Mostrar notas de qual aluno: (999 interrompe) '))
    if pergunta == 999:
        break
    print(f'Notas de {alunos[pergunta][0]} são: {alunos[pergunta][1]}')
    