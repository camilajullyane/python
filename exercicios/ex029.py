velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! Você deve pagar uma multa de R$ {multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')