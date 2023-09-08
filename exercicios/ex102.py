def fatorial(num=1, show = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end=' ')
    return f



numero = int(input('Digite um número: '))

#PROGRAMA PRINCIPAL
print(fatorial(numero))

