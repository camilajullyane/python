tupla = ('pao', 'banana', 'caderno')

for item in tupla:
    print(f'\nNa palavra {item} temos ', end='')
    for c in item:
        if c in 'aeiou':
            print(f'{c}', end=' ')

