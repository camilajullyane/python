def leiaInt(txt):
    n = (input(txt))
    if n.isnumeric():
        return n    
    else:
        print('[ERRO DE ENTRADA]')
        return leiaInt(txt)
    
n = leiaInt('Digite um número: ')
print(f'Você acabou digitar o número {n}')