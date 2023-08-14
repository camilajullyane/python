from datetime import date
ano = int(input('Informe o ano para análise! Digite 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')