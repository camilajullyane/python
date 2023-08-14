sal = float(input('Digite seu salário: '))

if sal > 1250:
    aumento = sal * 0.10
else:
    aumento = sal * 0.15
print(f'O seu aumento será de R$ {aumento:.2f}. O valor total passará a ser R$ {sal + aumento:.2f}')