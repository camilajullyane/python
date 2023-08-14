primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(10):
    primeiro += razao
    print(primeiro - razao, end= ' ')
