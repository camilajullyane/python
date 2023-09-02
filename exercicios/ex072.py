numeros = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


usuario = int(input('Digite um número entre 0 e 20: '))
while usuario not in range(0, 21):
    usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[usuario]}')
