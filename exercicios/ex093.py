pontuacao = []
total = 0
dicionario = {
    'nome': input('Nome do jogador: ')
    
}

partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    total += gols
    pontuacao.append(gols)
dicionario['gols'] = pontuacao[:]
dicionario['total'] = total


print('-='*30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*30)

print(f'O jogar {dicionario["nome"]} jogou {partidas}')
for p, v in enumerate(pontuacao):
    print(f'Na partida {p}, fez {v} gols')
print(total)