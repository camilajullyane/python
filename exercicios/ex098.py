from time import sleep

def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ', flush=True)
        sleep(0.5) 
    print('FIM!')

print('Contagem de 1 a 10 de 1 em 1')
contador(1, 11, 1)
print()

print('Contagem de 10 a 1 de 2 em 2')
contador(10, -1, -2)
print()

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
if pas == 0:
    pas = 1

print(f'Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}')
contador(ini, fim, pas)

