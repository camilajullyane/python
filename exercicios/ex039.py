from datetime import date
sexo = str(input('Informe seu sexo: ')).strip()
ano = int(input('Informe o ano em que você nasceu: '))

idade = date.today().year - ano # ANO ATUAL - ANO DE NASCIMENTO = IDADE DO USUÁRIO

if sexo == 'feminino':
    print('Você não precisa fazer o alistamento')
elif idade < 18:
    tempo = date.today().year + (18 - idade) # QUANTOS ANOS FALTAM PRA ELE COMPLETAR 18 + O ANO ATUAL = ANO DE ALISTAMENTO
    print(f'Você ainda vai se alistar. Seu alistamento será em {tempo}')
elif idade == 18:
    print('Você completou 18 anos. Está na hora de alistar IMEDIATAMENTE!')
else:
    tempo = idade - 18 
    ano = date.today().year - tempo
    print(f'Você passou dos 18 anos. Seu alistamento está {tempo} anos atrasado e deveria ter sido no ano de {ano}')
