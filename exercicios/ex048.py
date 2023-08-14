soma = 0
cont= 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        print(c)
print(f'A soma dos {cont} números que são múltiplos de 3 que estão entre 1 e 500 é: {soma}')

     


