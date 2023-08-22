print('=' *20)
print('BANCO CEV')
print('=' *20)
cinq = 0
vinte = 0
dez = 0
cinco = 0
um = 0
valor = int(input('Qual valor você quer sacar? '))
while True:  
    if valor % 50 == 0:
        cinq += 1
    elif valor % 20:
        vinte += 1
    elif valor % 10:
        dez += 1
    elif valor % 5 == 0:
        cinco += 1
    else:
        um += 1
print()
        