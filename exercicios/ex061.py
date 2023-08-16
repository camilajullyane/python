p1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão da PA? '))

cont = 1
while cont <= 10:
    p1 += r
    cont += 1
    print(f'{p1 - r} -> ', end= '')
print('Acabou')


