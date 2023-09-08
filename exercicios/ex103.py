def ficha(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    if g not in '123456789' or '':
        g = '0'
    print(f'O jogador {n} fez {g} gol(s)  no campeonato')


ficha(input('Nome do jogador: '), input('numero de Gols: '))