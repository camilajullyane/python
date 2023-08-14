frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1)) #adicionar +1 pra nao começar a contagem da posição 0
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))