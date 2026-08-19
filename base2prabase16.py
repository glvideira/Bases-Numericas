from conversores import base2prabase10

base2 = input('Digite um numero base 2: ')

if base2 in '23456789' or base2.isalpha():
    print('Número inválido')

else:
    base16 = list()
    grupos = list()
    posicaoBase2 = len(base2) - 1
    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(posicaoBase2, -1, -4):
        grupo = base2[max(0, i-3):i+1]
        grupos.insert(0, grupo)

    for grupo2 in grupos:
        grupo10 = base2prabase10(grupo2)
        if grupo10 in range(10, 16):
            grupo10 = letras[grupo10]

        base16.append(grupo10)

print(f'Convertendo {base2} em base 16:')
print(base2)
print('virou')
for c in base16:
    print(f'{c}', end='')
