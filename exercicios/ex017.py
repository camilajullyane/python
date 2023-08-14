# CÁLCULO DA HIPOTENUSA USANDO A BIBLIOTECA MATH

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = math.hypot(ca, co)

print(f'O comprimento da hipotenusa é igual a {h1:.2f}')



# CÁLCULO DA HIPOTENUSA USANDO A FÓRMULA MATEMÁTICA

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = (co**2 + ca**2)**0.5   #hip = (co**2 + ca**2)**(1/2)
print(f'O comprimento da hipotenusa é {hip:.2f}')'''