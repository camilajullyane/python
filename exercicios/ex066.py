cont = num = soma = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        print('FIM')
        break
    soma += num
    cont += 1
print(f'O total de números digitados foi {cont} e a soma entre eles é de {soma}')