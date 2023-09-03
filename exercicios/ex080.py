lista = []


for j in range(0, 5 ):
    valor = int(input('Digite um valor: '))
    if j == 0 or valor > lista[-1]:
        lista.append(valor)
    elif valor < lista[0]:
        lista.insert(0, valor)
    else:
        for c in range(len(lista)):
            if valor < lista[c]:
                lista.insert(c, valor)
                break

print(lista)
