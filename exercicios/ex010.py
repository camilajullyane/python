real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.77

print('Com R${} reais, você pode comprar R${:.2} dólares'.format(real, dolar))