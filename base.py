onibus = {}
cont = 0
poltrona = []


def cadastro(cont):
    onibus[f'passageiro {cont}'] = {
        'nome' : input('Nome: '),
        'rg' : input('RG: '),
        'destino' : input('Destino: '),
        'origem' : input('Origem: '),
        'poltrona': verifica(cont)
    }
    poltrona.append(onibus[f'passageiro{cont}']['poltrona'])


def lista():
    for k,v  in onibus.items():
        print(f'{k} : {v}')


def modificar(p):
    print('''
        [1] Destino
        [2] Origem
        [3] Poltrona
        [4] Sair
''')
    res2 = int(input('O que você deseja modificar? '))
    match res2:
        case 1:
            onibus[f'passageiro{p}']['destino'] = input('Novo destino: ') 
        case 2:
            onibus[f'passageiro{p}']['origem'] = input('Nova origem: ')
        case 3:
            verifica(p)
        case 4:
            print('Saindo...')

def verifica(p):
        while True:
            novapol = int(input('Nova poltrona: '))
            if novapol in poltrona:
                    print('Poltrona ocupada. Escolha outro lugar!')
            else:
                onibus[f'passageiro{p}']['poltrona'] = novapol
                break

while True:
    print('''
        [1] Cadastro
        [2] Lista
        [3] Modificar passagem
        [4] Sair 
''')
    res = int(input('Escolha uma opção: '))
    match res:
        case 1:
            cont += 1
            cadastro(cont)
        case 2:
            lista()
        case 3:
            lista()
            per = int(input('Qual passageiro você deseja modificar? '))
            modificar(per)
        case 4:
            break