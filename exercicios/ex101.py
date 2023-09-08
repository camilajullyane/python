from datetime import date

def voto(ano_nasc):
    idade = ano_atual - ano_nasc
    if idade < 18:
        return 'NÃO VOTA'
    elif idade > 65:
        return 'VOTO OPCIONAL'
    elif idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
print(f'Com {ano_atual - ano_nascimento} anos: {voto(ano_nascimento)}')
