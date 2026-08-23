# Base 2 ///////////////////////////////////////////
def base2prabase10(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if any(c not in '01' for c in base2):
        print('Valor inválido. Só pode conter os dígitos 0 e 1.')
        return

    base10 = 0
    posicoes = list()
    tamanhoBase2 = len(base2) - 1

    while tamanhoBase2 > -1:
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


def base2prabase16(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if any(c not in '01' for c in base2):
        print('Valor inválido. Só pode conter os dígitos 0 e 1.')
        return

    base16 = list()
    grupos = list()
    posicaoBase2 = len(base2) - 1
    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(posicaoBase2, -1, -4):
        grupo = base2[max(0, i - 3):i + 1]
        grupos.insert(0, grupo)

    for grupo2 in grupos:
        grupo10 = base2prabase10(grupo2)
        if grupo10 in range(10, 16):
            grupo10 = letras[grupo10]

        base16.append(grupo10)

    if textoFinal:
        print(f'Convertendo {base2} em base 16:')
        print(base2)
        print('virou')
        for c in base16:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base16)


def base2prabase8(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if any(c not in '01' for c in base2):
        print('Valor inválido. Só pode conter os dígitos 0 e 1.')
        return

    base8 = list()
    grupos = list()
    posicaoBase2 = len(base2) - 1

    for i in range(posicaoBase2, -1, -3):
        grupo = base2[max(0, i - 2):i + 1]
        grupos.insert(0, grupo)

    for grupo2 in grupos:
        grupo10 = base2prabase10(grupo2)
        base8.append(grupo10)

    if textoFinal:
        print(f'Convertendo {base2} em base 8:')
        print(base2)
        print('virou')
        for c in base8:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base8)


# Base 10 ///////////////////////////////////////////

def base10prabase2(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True
    else:
        base10 = int(base10)  # aceita string vinda de outra função/gerenciador

    base2 = list()
    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 2
        base2.insert(0, resto)
        numeroAtual = numeroAtual // 2

    if not base2:
        base2 = [0]

    if textoFinal:
        print(f'Convertendo {base10} em base 2:')
        print(base10)
        print('virou')
        for c in base2:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base2)


def base10prabase16(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True
    else:
        base10 = int(base10)

    base16 = list()
    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 16
        if resto in range(10, 16):
            resto = letras[resto]
        base16.insert(0, resto)
        numeroAtual = numeroAtual // 16

    if not base16:
        base16 = [0]

    if textoFinal:
        print(f'Convertendo {base10} em base 16:')
        print(base10)
        print('virou')
        for c in base16:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base16)


def base10prabase8(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True
    else:
        base10 = int(base10)

    base8 = list()
    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 8
        base8.insert(0, resto)
        numeroAtual = numeroAtual // 8

    if not base8:
        base8 = [0]

    if textoFinal:
        print(f'Convertendo {base10} em base 8:')
        print(base10)
        print('virou')
        for c in base8:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base8)


# Base 16 ///////////////////////////////////////////

def base16prabase10(base16=None):
    textoFinal = False
    if base16 is None:
        base16 = input('Digite um numero base 16: ').upper()
        textoFinal = True

    if any(c in 'GHIJKLMNOPQRSTUVWXYZ' for c in base16):
        print('Valor inválido')
        return

    base10 = 0
    numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    posicoes = list()
    base16Valores = list()
    tamanhoBase16 = len(base16) - 1

    for c in base16:
        if c.isalpha():
            base16Valores.append(numeros[c])
        else:
            base16Valores.append(c)

    while tamanhoBase16 > -1:
        posicoes.append(tamanhoBase16)
        tamanhoBase16 -= 1

    for pos, numero in enumerate(posicoes):
        base10 += int(base16Valores[pos]) * 16 ** numero

    if textoFinal:
        print(f'Convertendo {base16} em base 10:')
        print(base16)
        print('virou')
        print(base10)
    else:
        return base10


def base16prabase2(base16=None):
    textoFinal = False
    if base16 is None:
        base16 = input('Digite um numero base 16: ').upper()
        textoFinal = True

    if any(c in 'GHIJKLMNOPQRSTUVWXYZ' for c in base16):
        print('Valor inválido')
        return

    numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    base2 = list()
    tamanhoBase16 = len(base16)

    for c in range(0, tamanhoBase16):
        if base16[c].isalpha():
            base2.append(base10prabase2(numeros[base16[c]]))
        else:
            base2.append(base10prabase2(int(base16[c])))

    if textoFinal:
        print(f'Convertendo {base16} em base 2:')
        print(base16)
        print('virou')
        for c in base2:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base2)


# Base 8 ///////////////////////////////////////////

def base8prabase10(base8=None):
    textoFinal = False
    if base8 is None:
        base8 = input('Digite um numero base 8: ')
        textoFinal = True

    if any(c not in '01234567' for c in base8):
        print('Valor inválido. Só pode conter dígitos de 0 a 7.')
        return

    base10 = 0
    posicoes = list()
    tamanhoBase8 = len(base8) - 1

    while tamanhoBase8 > -1:
        posicoes.append(tamanhoBase8)
        tamanhoBase8 -= 1

    for pos, numero in enumerate(posicoes):
        base10 += int(base8[pos]) * 8 ** numero

    if textoFinal:
        print(f'Convertendo {base8} em base 10:')
        print(base8)
        print('virou')
        print(base10)
    else:
        return base10


def base8prabase2(base8=None):
    textoFinal = False
    if base8 is None:
        base8 = input('Digite um numero base 8: ')
        textoFinal = True

    if any(c not in '01234567' for c in base8):
        print('Valor inválido. Só pode conter dígitos de 0 a 7.')
        return

    base2 = list()
    tamanhoBase8 = len(base8)

    for c in range(0, tamanhoBase8):
        base2.append(base10prabase2(int(base8[c])))

    if textoFinal:
        print(f'Convertendo {base8} em base 2:')
        print(base8)
        print('virou')
        for c in base2:
            print(f'{c}', end='')
        print()
    else:
        return ''.join(str(c) for c in base2)


# Conversor Universal ///////////////////////////////////////////

def conversorUniversal(baseOrigem, baseDestino, numero):
    """
    CONVERSOR UNIVERSAL
    baseOrigem : primeira base
    baseDestino : segunda base
    numero : numero na primeira base que será convertido na segunda
    
    A base máxima aceita no conversor universal é a base 36.
    """
    if baseOrigem < 2 or baseDestino < 2:
        print('Base inválida. As bases devem ser maiores ou iguais a 2.')
        return

    if baseOrigem > 36 or baseDestino > 36:
        print('Base inválida. As bases não podem ser maiores que 36.')
        return

    numeros = {}
    if baseOrigem > 10:
        numeros = {chr(65 + i): i + 10 for i in range(min(baseOrigem - 10, 26))}

    if any(c.isalpha() for c in numero):
        if baseOrigem <= 10:
            print('Número inválido. Só pode conter letras a partir da base 11.')
            return
        if any(c.isalpha() and c not in numeros for c in numero):
            print(f'Número inválido. Uma das letras não é válida para a base {baseOrigem}')
            return

    base10 = 0
    posicoes = list()
    valoresNumero = list()
    tamanhoNumero = len(numero) - 1

    for c in numero:
        if c.isalpha():
            valoresNumero.append(numeros[c])
        else:
            valoresNumero.append(int(c))

    for v in valoresNumero:
        if v < 0 or v >= baseOrigem:
            print(f'Número inválido. Não pode ser menor que 0 ou maior/igual a {baseOrigem}')
            return

    while tamanhoNumero > -1:
        posicoes.append(tamanhoNumero)
        tamanhoNumero -= 1

    for valor, pos in zip(valoresNumero, posicoes):
        "soma das potências"
        base10 += valor * baseOrigem ** pos

    if baseDestino == 10:
        print(f'{base10}')
        return

    letras = {i + 10: chr(65 + i)  for i in range(min(baseOrigem - 10, 26))}
    numeroFinal = list()
    dividendo = base10

    while dividendo > 0:
        resto = dividendo % baseDestino
        if resto >= 10:
            resto = letras[resto]
        numeroFinal.insert(0, str(resto))
        dividendo = dividendo // baseDestino

    if not numeroFinal:
        numeroFinal = ['0']

    print(''.join(numeroFinal))


# Gerenciador das Conversões ///////////////////////////////////////////
def gerenciadorConversoes():
    baseOrigem = int(input('Digite a base de origem: '))
    baseDestino = int(input('Digite a base de destino: '))
    numero = input(f'Digite o número da base {baseOrigem}: ').upper().strip()

    match baseOrigem:
        case 2:
            match baseDestino:
                case 10:
                    return base2prabase10(numero)
                case 16:
                    return base2prabase16(numero)
                case 8:
                    return base2prabase8(numero)
                case _:
                    return conversorUniversal(baseOrigem, baseDestino, numero)
        case 10:
            match baseDestino:
                case 2:
                    return base10prabase2(numero)
                case 16:
                    return base10prabase16(numero)
                case 8:
                    return base10prabase8(numero)
                case _:
                    return conversorUniversal(baseOrigem, baseDestino, numero)
        case 16:
            match baseDestino:
                case 10:
                    return base16prabase10(numero)
                case 2:
                    return base16prabase2(numero)
                case _:
                    return conversorUniversal(baseOrigem, baseDestino, numero)
        case 8:
            match baseDestino:
                case 10:
                    return base8prabase10(numero)
                case 2:
                    return base8prabase2(numero)
                case _:
                    return conversorUniversal(baseOrigem, baseDestino, numero)
        case _:
            return conversorUniversal(baseOrigem, baseDestino, numero)
