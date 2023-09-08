'''def ajuda(txt):
        help(txt)
        

def pergunta():
    while True:
        comando = input('Função ou biblioteca > ')
        if comando == 'FIM':
             print('PROGRAMA ENCERRADO')
             break
        else:
             ajuda(comando)


pergunta()'''


#COM RECURSIVIDADE

def ajuda(txt):
        help(txt)
        

def pergunta():
    comando = input('Função ou biblioteca > ')
    if comando == 'FIM':
        print('PROGRAMA ENCERRADO')
    else:
        ajuda(comando)
        pergunta()


pergunta()