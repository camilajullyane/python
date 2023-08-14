a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and c + a > b:
    print(f'Os segmentos acima PODEM formar um triângulo ', end='') # O COMANDO end ='' É USADO PARA QUE NÃO TENHA NADA NO FINAL DA LINHA.
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b and a != c and c != b:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('NÃO PODEM FORMAR um triângulo')
