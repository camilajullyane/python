d = int(input('Qual a distância da viagem? '))
print(f'Você está prestes a fazer uma viagem de {d} Km')
if d <= 200:
    preço = 0.50 * d
else:
    preço = 0.45 * d
    
print(f'Sua passagem custa R$ {preço:.2f}')   
