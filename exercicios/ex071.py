print('=' *20)
print('BANCO CEV')
print('=' *20)

ced = 50
saque = float(input('Qual o valor do seu saque? '))
contagem_ced = 0
total = saque


while True:
    if total >= ced:
        total -= ced
        contagem_ced += 1
    else:
        if contagem_ced > 0:
            print(f'{contagem_ced} cédulas de {ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contagem_ced = 0
        if total == 0:
            break
        
            
            
        


            

        
