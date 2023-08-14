frase = 'Curso em vídeo python'
frase = frase.replace('Curso', 'Aula')
print(frase[0:20])
print(frase[9:21:3]) #começar a contar do 9 até o 21 e pulando de 3 em 3
print(frase[::2])
print(frase.count('o')) #ele vai mostrar a quantidade de vezes que a letra 'o' está aparecendo na string
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Curso', 'Aula'))
print('Curso' in frase) #verifica se a palavra 'Curso' está presente na variável frase, ele retorna True se for verdadeiro e False se for falso
print(frase.find('Curso')) #mostra a posição em que a palavra 'Curso' é iniciada
dividido = frase.split()
print(dividido)
print(dividido[0]) #vai mostrar apenas o nome na posição 0 da lista
print(dividido[2][3]) #mostra na palavra 2 o que está escrito na posição 3, ou seja, é uma posição dentro de outra