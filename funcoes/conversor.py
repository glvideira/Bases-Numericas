from time import sleep
from random import randint, choice
from rich.console import Console
from rich.table import Table
import funcoes.menus as menu
from textwrap import dedent

class NumeroInvalidoError(Exception):
    'Erro lançado quando algum dos números nos parâmetros do conversor universal estão errados'
    pass

console = Console()

def tutorial():
    while True:
        console.clear()
        tabela = Table(title="Conversor de Bases")

        tabela.add_column("Opção", style="cyan", justify="center")
        tabela.add_column("Conversão", style="white")

        tabela.add_row("1", "Qualquer base para base 10")
        tabela.add_row("2", "Base 10 para outra base")
        tabela.add_row("3", "Base 2 para base 8 / 16")
        tabela.add_row("4", "Base 8/16 para base 2")
        tabela.add_row("5", "Conversão Geral")
        tabela.add_row("0", "Voltar")

        console.print(tabela)

        escolha = menu.escolha_menu()
        print(dedent('''\

            '''))

        console.clear()
        match escolha:
            case 1:
                print(dedent('''\
                    Multiplique cada dígito do número pela base a ser convertida elevado à potência da sua posição (começando da direita):

                    .... + a2 × b² + a1 × b¹ + a0 × b⁰

                    Exemplo:

                    Quero passar 101 (base 2) para base 10:
                    1 × 2² + 0 × 2¹ + 1 × 2⁰ =
                    4 + 0 + 1 = 5 (base 10)

                    Esse método é chamado de soma das potências.
                '''))
            
            case 2:
                print(dedent('''\
                    Divida o número na base 10 pela base desejada sucessivamente até o quociente ser 0. O resultado na base desejada é formada pelos restos da divisão lidos de trás pra frente.

                    Exemplo:

                    Quero passar 160 (base 10) para base 16:

                    160| 16
                    0    10| 16
                         10   0

                    Resultado: A0 h

                    Lembrando: números acima de 9 viram letras (10  = A, 11 = B, 12 = C...).
                            '''))

            case 3:
                print(dedent('''\
                    Separe a sequência binária em grupos de 3 / 4 algarismos (base 8 e base 16, respectivamente), da direita para a esquerda

                    Exemplo:

                    11111101 (base2)

                    Passe cada grupo para base 10 e junte no final:

                    para base 8: 0011 111 101 2 = 375 (base 8);
                    para base 16: 1111 1101 2 = FD h.
                            '''))

            case 4:
                print(dedent('''\
                    Separe os algarismos e faça a divisão para descobrir o correspondente em binário.

                    Exemplo:
                    375 (base 8)

                    3| 2               7| 2               5| 2
                    1  1| 2            1  3| 2            1  2| 2
                       1  0               1  1| 2            0  1| 2
                                             1  0               1  0

                    Resultado: 011111101 (base 2)
            '''))
                
            case 5:
                print(dedent('''\
                    1. Converter uma base A para base 10 (usando soma das potências)
                    2. Converter da base 10 para base B (dividindo e pegando o resto)

                    Com isso, podemos converter bases com números diferentes, como base 5 para base 9.
            '''))

            case 0:
                return
            
        print()
        sleep(1.5)
        input('Pressione enter para continuar')


def geradorBases():
    while True:
        console.clear()
        print('1 – Praticar apenas com bases 2, 8, 10, 16')
        print('2 – Praticar com diferentes bases (2 a 20)')
        print('0 - voltar')

        escolha = menu.escolha_menu()
        
        console.clear()
        match escolha:
            case 1:
                bases = [2, 8, 10, 16]
                numero = randint(1, 999)
                
                base1 = choice(bases)
                bases.remove(base1)
                base2 = choice(bases)

                if base1 != 10:
                    numero = conversorUniversal(10, base1, str(numero))

                resposta = conversorUniversal(base1, base2, str(numero))

                print(f'Passe {numero} (base {base1}) para a base {base2}.')
                respostaUsuario = input('Resposta: ').strip().upper()

                respostaUsuario = respostaUsuario.lstrip('0') or '0'

                if respostaUsuario == resposta:
                    print('resposta correta!')
                    
                else:
                    print('Resposta incorreta!')
                    sleep(0.7)
                    print(f'O resultado era {resposta}')

                continuar = input('Tentar novamente? [s/n] ').strip().lower()
                if continuar != 's':
                    return

            case 2:
                bases = list(range(2, 21))
                numero = randint(1, 999)

                base1 = choice(bases)
                bases.remove(base1)
                base2 = choice(bases)

                if base1 != 10:
                    numero = conversorUniversal(10, base1, str(numero))

                resposta = conversorUniversal(base1, base2, str(numero))

                print(f'Passe {numero} (base {base1}) para a base {base2}.')
                respostaUsuario = input('Resposta: ').strip().upper()

                respostaUsuario = respostaUsuario.lstrip('0') or '0'

                if respostaUsuario == resposta:
                    print('resposta correta!')
                    
                else:
                    print('Resposta incorreta!')
                    sleep(0.7)
                    print(f'O resultado era {resposta}')

                continuar = input('Tentar novamente? [s/n] ').strip().lower()
                if continuar != 's':
                    return
            case 0:
                return
            
def conversorUniversal(baseOrigem, baseDestino, numero):
    """
    CONVERSOR UNIVERSAL
    baseOrigem : primeira base
    baseDestino : segunda base
    numero : número na primeira base que será convertido na segunda
    
    A base máxima aceita no conversor universal é a base 36.
    """
    if not numero: 
        raise NumeroInvalidoError('Número inválido. Nenhum número foi digitado.')
    
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

    # Se n for uma letra, a (valoresNumero) recebe o valor de {letras} de acordo com a letra
    for n in numero:
        if n.isalpha():
            valoresNumero.append(letras[n])
        elif n.isdigit():
            valoresNumero.append(int(n))
        else:
            raise NumeroInvalidoError(f'Número inválido. O caractere "{n}" não é válido.')
    

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
        return str(base10)

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

            print()
            print(f'Valor {numero}')
            print(f'base {baseOrigem}')
            print(f'Para')
            print(f'base {baseDestino}')
            print()
            print(f'vira {numeroConvertido}')
            sleep(1)

            continuar = input('Converter outro número? [s/n]: ').strip().lower()
            if continuar != 's':
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
