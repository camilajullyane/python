dias = int(input('Quantos alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = (60 * dias) + (0.15 * km)
print(f'O total a pagar é de R${aluguel:.2f}')