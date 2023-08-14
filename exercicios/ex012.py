prod = float(input('Qual o preço do produto? '))
desc = (prod * 5)/100
atual = prod - desc
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(prod, atual))