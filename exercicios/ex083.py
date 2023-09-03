aberta = []
fechado = []

expre = str(input('Digite a expressão: '))

for c in expre:
    if c in '(':
        aberta.append('(')
    elif c in ')':
        fechado.append(')')


if len(aberta) == len(fechado):
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')