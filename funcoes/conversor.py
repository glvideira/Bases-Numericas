from time import sleep

class NumeroInvalidoError(Exception):
    'Erro lançado quando algum dos números nos parâmetros do conversor universal estão errados'
    pass

def conversorUniversal(baseOrigem, baseDestino, numero):
    """
    CONVERSOR UNIVERSAL
    baseOrigem : primeira base
    baseDestino : segunda base
    numero : número na primeira base que será convertido na segunda
    
    A base máxima aceita no conversor universal é a base 36.
    """

    if baseOrigem < 2 or baseDestino < 2:
        raise NumeroInvalidoError('Base inválida. As bases devem ser maiores ou iguais a 2.')

    if baseOrigem > 36 or baseDestino > 36:
        raise NumeroInvalidoError('Base inválida. As bases não podem ser maiores que 36.')
    
    # Dicionário das letras é feito a partir da base de origem, se for base 10, terá apenas A: 10, se for 36, terá o alfabeto inteiro
    letras = {} if baseOrigem <= 10 else {chr(65 + i): i + 10 for i in range(min(baseOrigem - 10, 26))}
    numero = numero.upper().strip()
    
    if any(c.isalpha() for c in numero):
        if baseOrigem <= 10:
            raise NumeroInvalidoError('Número inválido. Só pode conter letras a partir da base 11.')
        if any(c.isalpha() and c not in letras for c in numero):
            raise NumeroInvalidoError(f'Número inválido. Uma das letras não é válida para a base {baseOrigem}')


    base10 = 0
    posicoes = list()
    valoresNumero = list()
    tamanhoNumero = len(numero) - 1

    # Se c for uma letra, a (valoresNumero) recebe o valor de {letras} de acordo com a letra

    

    for c in numero:
        if c.isalpha():
            valoresNumero.append(letras[c])
        elif c.isdigit():
            valoresNumero.append(int(c))
        else:
            raise NumeroInvalidoError(f'Número inválido. O caractere "{c}" não é válido.')
    

    for v in valoresNumero:
        if v < 0 or v >= baseOrigem:
            raise NumeroInvalidoError(f'Número inválido. Não pode ser menor que 0 ou maior/igual a {baseOrigem}')

    while tamanhoNumero > -1:
        posicoes.append(tamanhoNumero)
        tamanhoNumero -= 1

    # Soma das potências
    for valor, pos in zip(valoresNumero, posicoes):
        base10 += valor * baseOrigem ** pos
    

    if baseDestino == 10:
        return base10

    # Mesmo esquema de {letras}, mas ao contrário 10: A, 11: B...
    numeros = {i + 10: chr(65 + i)  for i in range(min(baseDestino - 10, 26))}

    numeroFinal = list()
    dividendo = base10

    # Divisão da base 10
    while dividendo > 0:
        resto = dividendo % baseDestino
        if resto >= 10:
            resto = numeros[resto]
        numeroFinal.insert(0, str(resto))
        dividendo = dividendo // baseDestino

    if not numeroFinal:
        numeroFinal = ['0']

    numeroFinal = ''.join(numeroFinal)
    
    return numeroFinal


# Gerenciador das Conversões ///////////////////////////////////////////
def gerenciadorConversoes():
    while True:
        try:
            baseOrigem = int(input('Digite a base de origem: '))
            baseDestino = int(input('Digite a base de destino: '))
            numero = input(f'Digite o número da base {baseOrigem}: ')

            numeroConvertido = conversorUniversal(baseOrigem, baseDestino, numero)

            print(f'{numeroConvertido}')
            return


        except ValueError:
            print('Erro: em umas das bases foi digitado um caractér inválido, tente novamente.')
            sleep(1.5)
        except NumeroInvalidoError as e:
            print(f'Erro: {e}')
            sleep(1.5)
        except Exception as e:
            print(f'Erro: {e}')
            sleep(1.5)
