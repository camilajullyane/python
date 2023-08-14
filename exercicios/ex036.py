casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar a casa? '))



exc = sal * 0.30 #VALOR MÁXIMO QUE A PRESTAÇÃO PODE ASSUMIR
valor_prest = casa / (anos * 12)

if valor_prest <= exc:
    print(f'Parbéns, seu empréstimo foi aprovado! O valor da parcela mensal ficará de R${valor_prest:.2f}')
else:
    print('Sinto muito! Sua solitição de empréstimo foi negada.')