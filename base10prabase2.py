base10 = int(input('Digite um numero base 10: '))

base2 = list()

numeroAtual = base10

while numeroAtual > 0:
    resto = numeroAtual % 2
    base2.insert(0, resto)
    numeroAtual = numeroAtual // 2

print(f'Convertendo {base10} em base 2:')
print(base10)
print('virou')
for c in base2:
    print(f'{c}', end='')
