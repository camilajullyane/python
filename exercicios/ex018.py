import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O valor do SENO é {sen:.2f}')
print(f'O valor do COSSENO é {cos:.2f}')
print(f'O valor da TANGENTE é {tg:.2f}')