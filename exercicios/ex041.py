from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade}')

if idade <= 9:
    print('Você se classifica como MIRIM')
elif idade <= 14:
    print('Você se classifica como INFANTIL')
elif idade <= 19:
    print('Você se classifica como JUNIOR')
elif idade <= 25:
    print('Você se classifica como SÊNIOR')
else:
    print('Você se classifica como MASTER')
