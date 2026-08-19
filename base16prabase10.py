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
