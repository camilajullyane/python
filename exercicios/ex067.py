num = 0

while True:
    res = int(input('Quer ver a tabuada de qual valor? '))
    if res < 0:
        print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
        break
    for c in range(11):
        print(f'{res} x {c} = {res * c}')
    