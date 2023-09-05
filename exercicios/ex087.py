matriz = []
cont = 0
soma = 0
soma_col = 0

maior = menor = 0

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        valor = int(input(f'Digite um valor para a posição[{linha},{coluna}]: '))
        matriz[linha].append(valor)

        if valor % 2 == 0:
            soma += valor

        if coluna == 2:
            soma_col += matriz[linha][coluna]
        
            

for c, v in enumerate(matriz):
    if c == 1:
        maior = v[0]
    elif maior < v[1]:
        maior = v[1]
    elif maior < v[2]:
        maior = v[2]

for c in matriz:
    for i in c:
        print(f'[ {i} ]', end='')
    print('\n')

print(soma)
print(soma_col)
print(f'O maior valor da segunda linha foi {maior}')