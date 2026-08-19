
base2 = input('Digite um numero base 2: ')

if base2 in '23456789' or base2.isalpha():
    print('Número inválido')

else:
    base10 = 0

    posicoes = list()

    tamanhoBase2 = len(base2) - 1

    while tamanhoBase2 > - 1:
        posicoes.append(tamanhoBase2)
        tamanhoBase2 -= 1

    for pos, numero in enumerate(posicoes):
        base10 += int(base2[pos]) * 2 ** numero

    print(f'Convertendo {base2} em base 10:')
    print(base2)
    print('virou')
    print(base10)
