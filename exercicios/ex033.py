a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# VERIFICANDO QUAL O MENOR NÚMERO
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# VERIFICANDO QUAL O MAIOR NÚMERO
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é {maior} e o menor número é {menor}')