matriz = []
cont = 0
soma = 0
soma_col = 0

maior = 0

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        valor = int(input(f'Digite um valor para a posição[{linha},{coluna}]: '))
        matriz[linha].append(valor)

        if valor % 2 == 0:
            soma += valor

        if coluna == 2:
            soma_col += matriz[linha][coluna]
        
            

        if coluna == 2:
            maior = (max(matriz[linha]))

for c in matriz:
    for i in c:
        print(f'[ {i} ]', end='')
    print()

print(soma)
print(soma_col)
print(f'O maior valor da coluna 2 foi {maior}')