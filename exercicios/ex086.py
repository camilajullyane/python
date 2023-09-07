matriz = []
for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para a posição[{linha},{coluna}]: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end=' ')
    print()