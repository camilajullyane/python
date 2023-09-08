from time import sleep
def maior(*numeros):
    cont = 0
    maior = 0
    
    print('-='* 30)
    print('Analisando valores passados...')
    for n in numeros:
        cont += 1
        print(n, end=' ')
        if n > maior:
            maior = n
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')
    


maior(2, 6, 7, 8, 4)
maior(1,2,3)
maior(6)
maior()