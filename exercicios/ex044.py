valor = float(input('Preço das compras: R$'))

print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

pagamento = int(input('Qual a opção? '))

if pagamento == 1:
    desconto = valor * 0.10
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - desconto:.2f}')
elif pagamento == 2:
    desconto = valor * 0.05
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - desconto:.2f}')
elif pagamento == 3:
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela} SEM JUROS e custará R${valor} no total.')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = valor + (valor * 0.20)  # VALOR DO JUROS
    tot_parc = total / parcelas
    print(f'Sua compra de R${valor:.2f} será parcelada em {parcelas} de R${tot_parc:.2f} COM JUROS e custará {total:.2f} no final.')