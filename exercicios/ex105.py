def notas(*num, situ=False):
    soma = 0
    for c in num:
        soma += c
    
    d = {   
            'total': len(num),
            'maior': max(num),
            'menor': min(num),
            'media': soma / len(num)
            
        }
    if situ == True:
        if d['media'] >= 7:
            d['situação'] = 'BOA'
        elif d['media'] < 7:
            d['situação'] = 'RUIM'
    return d
    
   
valores = notas(3.5, 2.5, 6.5, 2, 7, 4, situ=True)
print(valores)