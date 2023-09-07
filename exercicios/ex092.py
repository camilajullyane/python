# adicionar a key 'aposentadoria' no dicionario caso o usuario possuir carteira de trabalho

from datetime import date
ano_atual = date.today().year

dicionario = {
    'nome': input('Nome: '),
    'idade': ano_atual - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))

}
if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: '))

for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')