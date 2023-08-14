sal = float(input('Qual o salário do funcionário? '))
desc = (sal * 15) / 100
atual = sal + desc
print('Um funcionário que ganhava R${}, com o aumento de 15% vai receber R${:.2f}'.format(sal, atual))