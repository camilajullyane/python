a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento : '))

if a + b > c and b + c > a and c + a > b:
    print('As três retas FORMAM um triângulo')
else:
    print('As três retas NÃO FORMAM um triângulo')