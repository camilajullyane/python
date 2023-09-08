pontuacao = []

total = 0
while True:
    dicionario = {
        'nome': input('Nome do jogador: '),
        'gols': []
    }

    partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c}? '))
        total += gols
        dicionario['gols'].append(gols)
    

    dicionario['total'] = total
    total = 0
    pontuacao.append(dicionario.copy())
    dicionario.clear()
    perg = input('Quer continuar? [S/N]').upper()
    if perg == 'N':
        break

print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":<15}')
for p, v in enumerate(pontuacao):
    print(f'{p:<5}{v["nome"]:<15}{str(v["gols"]):<15}{v["total"]:<15}')
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para] '))
    if dados == 999:
        break
    print(f'--LEVANTAMENTO DO JOGADOR {pontuacao[dados]["nome"]}')

    for p, v in enumerate(pontuacao[dados]['gols']):
        print(f'No jogo {p} fez {v} gols')