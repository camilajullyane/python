def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} é {a}m²')


larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)