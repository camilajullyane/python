n = int(input('Digite um número: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ',end= '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2 
    t2 = t3
    cont += 1
    print(f'-> {t3}', end= '')


'''n = int(input())
anterior = 0
atual = 1
i = 0

while i <= n:
    aux = atual + anterior
    anterior = atual
    atual = aux
    i += 1
    print(atual)'''