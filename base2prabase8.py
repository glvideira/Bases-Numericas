from conversores import base2prabase10

base2 = input('Digite um numero base 2: ')

if base2 in '23456789' or base2.isalpha():
    print('Número inválido')

else:
    base8 = list()
    grupos = list()
    posicaoBase2 = len(base2) - 1

    for i in range(posicaoBase2, -1, -3):
        grupo = base2[max(0, i-2):i+1]
        grupos.insert(0, grupo)

    for grupo2 in grupos:
        grupo10 = base2prabase10(grupo2)

        base8.append(grupo10)

print(f'Convertendo {base2} em base 8:')
print(base2)
print('virou')
for c in base8:
    print(f'{c}', end='')
