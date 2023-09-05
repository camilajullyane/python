matriz = []
for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para a posição[{linha},{coluna}]: ')))

for c in matriz:
    for i in c:
        print(f'[ {i} ]', end='')
    print('\n')