def base2prabase10(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

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

        if textoFinal:
            print(f'Convertendo {base2} em base 10:')
            print(base2)
            print('virou')
            print(base10)
        else:
            return base10

def base10prabase2():
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
    
def base10prabase16(base10=None):
    if base10 is None:
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

def base16prabase10():
    base16 = input('Digite um numero base 16: ').upper()

    if base16 in 'GHIJKLMNOPQRSTUVWXYZ':
        print('Valor inválido')

    else:
        base10 = 0

        letras = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        posicoes = list()

        base16Valores  = list()

        tamanhoBase16 = len(base16) - 1

        for c in base16:
            if c.isalpha():
                base16Valores.append(letras[c])
            else:
                base16Valores.append(c)

        while tamanhoBase16 > - 1:
            posicoes.append(tamanhoBase16)
            tamanhoBase16 -= 1

        for pos, numero in enumerate(posicoes):
            base10 += int(base16Valores[pos]) * 16 ** numero

        print(f'Convertendo {base16} em base 10:')
        print(base16)
        print('virou')
        print(base10)
