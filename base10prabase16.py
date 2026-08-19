base10 = int(input('Digite um numero base 10: '))

base16 = list()

letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

numeroAtual = base10

while numeroAtual > 0:
    resto = numeroAtual % 16

    if resto in range(10, 16):
        resto = letras[resto]

    base16.insert(0, resto)
    numeroAtual = numeroAtual // 16

print(f'Convertendo {base10} em base 16:')
print(base10)
print('virou')
for c in base16:
    print(f'{c}', end='')
