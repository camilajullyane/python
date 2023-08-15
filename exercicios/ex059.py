from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
rodar = True

while rodar:
    print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
    
      ''')
    op = int(input('Esolha uma opção: '))
    if op == 1:
        soma = n1 + n2
        print(f'O resultado de {n1} + {n2} é {soma}')
    elif op == 2:
        multi = n1 * n2
        print(f'O resultado de {n1} * {n2} é {multi}')
    elif op == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print(f'O maior número foi {maior} e o menor número foi {menor}')
        elif n1 < n2:
            maior = n2
            menor = n1
            print(f'O maior número foi {maior} e o menor número foi {menor}')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa. Volte sempre!')
        rodar = False