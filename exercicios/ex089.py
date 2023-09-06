def validar(texto):
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        res = str(input(texto)).upper
    return res
# matriz = []
matriz = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    for c in matriz:

    res = validar('[ERRO DE ENTRADA]. Quer continuar? [S/N] ')
    if res == 'N':
        break
    
matriz2 = [['Camila', [8, 8]] ]
