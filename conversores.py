# Única função que será utilizada de fato no programa é a universal, 

# Base 2 ///////////////////////////////////////////
def base2prabase10(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if base2 in '23456789' or base2.isalpha():
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

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

def base2prabase16(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if base2 in '23456789' or base2.isalpha():
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

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
    if textoFinal:
        print(f'Convertendo {base2} em base 16:')
        print(base2)
        print('virou')
        for c in base16:
            print(f'{c}', end='')
    else:
        return ''.join(str(c) for c in base16)

def base2prabase8(base2=None):
    textoFinal = False
    if base2 is None:
        base2 = input('Digite um numero base 2: ')
        textoFinal = True

    if base2 in '23456789' or base2.isalpha():
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

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

    if textoFinal:
        print(f'Convertendo {base2} em base 8:')
        print(base2)
        print('virou')
        for c in base8:
            print(f'{c}', end='')
    else:
        return ''.join(str(c) for c in base8)

# Base 10 ///////////////////////////////////////////

def base10prabase2(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True 

    base2 = list()

    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 2
        base2.insert(0, resto)
        numeroAtual = numeroAtual // 2

    if textoFinal:
        print(f'Convertendo {base10} em base 2:')
        print(base10)
        print('virou')
        for c in base2:
            print(f'{c}', end='')
    else:
        return ''.join(str(c) for c in base2)
    
def base10prabase16(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True

    base16 = list()

    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 16

        if resto in range(10, 16):
            resto = letras[resto]

        base16.insert(0, resto)
        numeroAtual = numeroAtual // 16

    if textoFinal:
        print(f'Convertendo {base10} em base 16:')
        print(base10)
        print('virou')
        for c in base16:
            print(f'{c}', end='')
    else:
        return ''.join(str(c) for c in base16)

def base10prabase8(base10=None):
    textoFinal = False
    if base10 is None:
        base10 = int(input('Digite um numero base 10: '))
        textoFinal = True

    base8 = list()

    numeroAtual = base10

    while numeroAtual > 0:
        resto = numeroAtual % 8
        base8.insert(0, resto)
        numeroAtual = numeroAtual // 8

    if textoFinal:
        print(f'Convertendo {base10} em base 8:')
        print(base10)
        print('virou')
        for c in base8:
            print(f'{c}', end='')
    else:
        return ''.join(str(c) for c in base8)

# Base 16 ///////////////////////////////////////////

def base16prabase10(base16=None):
    textoFinal = False
    if base16 is None:
        base16 = input('Digite um numero base 16: ').upper()
        textoFinal = True

    if base16 in 'GHIJKLMNOPQRSTUVWXYZ':
        return 'Valor inválido' if not textoFinal else print('Valor inválido')
        
    else:
        base10 = 0
        numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        posicoes = list()
        base16Valores  = list()
        tamanhoBase16 = len(base16) - 1

        for c in base16:
            if c.isalpha():
                base16Valores.append(numeros[c])
            else:
                base16Valores.append(c)

        while tamanhoBase16 > - 1:
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

    if base16 in 'GHIJKLMNOPQRSTUVWXYZ':
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

    else:
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
    else:
        return ''.join(str(c) for c in base2)

# Base 8 ///////////////////////////////////////////

def base8prabase10(base8=None):
    textoFinal = False
    if base8 is None:
        base8 = input('Digite um numero base 8: ')
        textoFinal = True

    if base8 in '89' or base8.isalpha():
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

    else:
        base10 = 0

        posicoes = list()

        tamanhoBase8 = len(base8) - 1

        while tamanhoBase8 > - 1:
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

    if base8 in '89' or base8.isalpha():
        return 'Valor inválido' if not textoFinal else print('Valor inválido')

    else:
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
    else:
        return ''.join(str(c) for c in base2)

# Conversor Universal ///////////////////////////////////////////

def conversorUniversal(baseOrigem, baseDestino, numero):
    numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    base10 = 0
    posicoes = list()
    valoresNumero = list()
    tamanhoNumero = len(numero) - 1

    for c in numero:
        "parametro numero vai receber uma string, esse for transforma cada valor na string em int e coloca na lista valoresNumeros"
        if c.isalpha():
            valoresNumero.append(numeros[c])
        else:
            valoresNumero.append(int(c))

    while tamanhoNumero > - 1:
        "pega a posição certa de cada valor para usar na parte da soma das potências"
        posicoes.append(tamanhoNumero)
        tamanhoNumero -= 1

    for pos, valor in zip(posicoes, valoresNumero):
        "soma das potências"
        base10 += valor * baseOrigem ** pos

    if baseDestino == 10:
        return print(f'{base10}')

    letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    numeroFinal = list()
    dividendo = base10
    
    while dividendo > 0:
        resto = dividendo % baseDestino
        if resto in range(10, baseDestino):
                    resto = letras[resto]

        numeroFinal.insert(0, str(resto))
        dividendo = dividendo // baseDestino
    numeroFinal = ''.join(numeroFinal)

    return print(f'{numeroFinal}')

# Gerenciador das Conversões ///////////////////////////////////////////
def gerenciadorConversoes():
    baseOrigem = int(input('Digite a base de origem: '))
    if baseOrigem not in [2, 10, 16, 8]:
        return print('Base de origem inválida')
    baseDestino = int(input('Digite a base de destino: '))
    if baseDestino not in [2, 10, 16, 8]:
        return print('Base de destino inválida')
    numero = input('Digite o número a ser convertido: ')

    match baseOrigem:
        case 2:
            match baseDestino:
                case 10:
                    return base2prabase10(numero)
                case 16:
                    return base2prabase16(numero)
                case 8:
                    return base2prabase8(numero)
        case 10:
            match baseDestino:
                case 2:
                    return base10prabase2(numero)
                case 16:
                    return base10prabase16(numero)
                case 8:
                    return base10prabase8(numero)
        case 16:
            match baseDestino:
                case 10:
                    return base16prabase10(numero)
                case 2:
                    return base16prabase2(numero)
        case 8:
            match baseDestino:
                case 10:
                    return base8prabase10(numero)
                case 2:
                    return base8prabase2(numero)
        