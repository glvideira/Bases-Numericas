import funcoes.conversor as conv
from rich.console import Console
from rich.table import Table
import funcoes.menus as menu
from time import sleep
from random import randint
from textwrap import dedent
import os

console = Console()

def tutorialOperacoes():
    while True:
        os.system('cls')
        tabela = Table(title="Como calcular as operações")
            
        tabela.add_column("Opção", style="cyan", justify="center")
        tabela.add_column("Conversão", style="white")

        tabela.add_row("1", "Adição")
        tabela.add_row("2", "Subtração")
        tabela.add_row("3", "Multiplicação")
        tabela.add_row("4", "Divisão")
        tabela.add_row("0", "Sair")

        console.print(tabela)

        escolha = menu.escolha_menu()

        os.system('cls')
        match escolha:
            case 1:
                print(dedent('''\
                    ADIÇÃO EM BINÁRIO

                    Regras:
                    0 + 0 = 0
                    0 + 1 = 1
                    1 + 0 = 1
                    1 + 1 = 0 (vai 1 para o algarismo de ordem superior)
                    1 + 1 + 1 = 1 (vai 1 para o algarismo de ordem superior)

                    Exemplo:
                      1011   (11 em decimal)
                    +  110   ( 6 em decimal)
                    ——————
                     10001   (17 em decimal)
                    '''))

            case 2:
                print(dedent('''\
                    SUBTRAÇÃO EM BINÁRIO

                    Regras:
                    0 - 0 = 0
                    1 - 0 = 1
                    1 - 1 = 0
                    0 - 1 = 1   (vem 10 (um zero) do algarismo de ordem superior, 
                                    que representa o valor 2 em decimal)

                    Exemplo:
                      1011   (11 em decimal)
                    -  110   ( 6 em decimal)
                    ——————
                      0101   ( 5 em decimal)

                    Observação:

                          Minuendo
                    -   Subtraendo
                    ——————————————
                    Resto ou diferença

                    Caso o Minuendo seja menor que o subtraendo, troque os dois 
                    de posição e coloque um sinal negativo na diferença.
                    '''))
            case 3:
                print(dedent('''\
                    MULTIPLICAÇÃO EM BINÁRIO

                    A multiplicação de números binários segue o mesmo raciocínio da
                    multiplicação com números decimais.

                    1 * 1 = 1
                    1 * 0 = 0
                    0 * 1 = 0
                    0 * 0 = 0

                    Exemplo: 101 (5) x 11 (3)

                      101
                    x  11
                    ——————
                      101      (101 x 1, bit menos significativo)
                     101       (101 x 1, deslocado 1 casa à esquerda)
                    ——————
                     1111     (soma das linhas = 15 em decimal)
                    '''))
            case 4:
                print(dedent('''\
                    DIVISÃO EM BINÁRIO

                    Segue o mesmo processo da divisão longa decimal, mas
                    comparando apenas com 0 ou 1 em cada passo (nunca precisa
                    "tentar" um dígito de 2 a 9, só existe 0 ou 1 como
                    possibilidade).

                    Exemplo: 1011 (11) ÷ 10 (2)

                    1. Compara os primeiros bits do dividendo com o divisor.
                        Se o pedaço atual for >= divisor, o bit do quociente
                        é 1 e subtrai o divisor; senão, o bit é 0.
                    2. Desce o próximo bit do dividendo e repete.

                        1011 ÷ 10:
                        10 (primeiros 2 bits) >= 10 -> quociente 1, resto 0
                        desce o próximo bit: 01
                        01 < 10 -> quociente 0, resto 01
                        desce o próximo bit: 011
                        011 >= 10 -> quociente 1, resto 001

                        10'1'1'| 10
                        -   10   101
                        ——————
                           011
                        -   10 
                        ——————
                             1

                        Quociente: 101 (5 em decimal)
                        Resto: 1 (1 em decimal)
                    '''))
            case 0:
                return
        sleep(1.5)
        print()
        input('Pressione enter para continuar')

def geradorOperacoes():
    while True:
            os.system('cls')
            tabela = Table(title="Praticar Operações")
                
            tabela.add_column("Opção", style="cyan", justify="center")
            tabela.add_column("Conversão", style="white")
    
            tabela.add_row("1", "Adição")
            tabela.add_row("2", "Subtração")
            tabela.add_row("3", "Multiplicação")
            tabela.add_row("4", "Divisão")
            tabela.add_row("0", "Sair")
    
            console.print(tabela)
    
            escolha = menu.escolha_menu()
    
            os.system('cls')
            while True:
                match escolha:
                    case 1:
                        valor1 = randint(10, 500)
                        valor2 = randint(10, 500)
                        operador = '+'

                    case 2:
                        valor1 = randint(10, 500)
                        valor2 = randint(10, 200)
                        operador = '-'
                    case 3:
                        valor1 = randint(10, 500)
                        valor2 = randint(5, 50)
                        operador = 'x'
                    case 4:
                        valor1 = randint(10, 500)
                        valor2 = randint(5, 32)
                        operador = '/'
                    case 0:
                        return

                resposta = calculadoraBinaria(int(bin(valor1)[2:]), int(bin(valor2)[2:]), operador)

                respostaUsuario = input(f'{bin(valor1)[2:]} {operador} {bin(valor2)[2:]} = ')

                if respostaUsuario == resposta:
                    print('Resposta correta!')
                else:
                    print('Resposta incorreta!')
                    sleep(0.7)
                    print()
                    print(f'O resultado era {resposta}')

                continuar = input('Tentar novamente? [s/n] ').strip().lower()
                if continuar != 's':
                    break

            

def calculadoraBinaria(valor1, valor2, operacao):
    if not set(str(abs(valor1))) <= {'0', '1'} or not set(str(abs(valor2))) <= {'0', '1'}:
        raise conv.NumeroInvalidoError('Um dos números contém um algarismo diferente de 0 ou 1.')

    valor1 = int(str(valor1), 2)
    valor2 = int(str(valor2), 2)

    match operacao:
        case "+":
            resposta = bin(valor1 + valor2)[2:]
        case "-":
            if valor1 > valor2:
                resposta = bin(valor1 - valor2)[2:]
            else:
                resposta = bin(valor1 - valor2)
                resposta = resposta[0] + resposta[3:]
        case "x":
            resposta = bin(valor1 * valor2)[2:]
        case "/":
            resposta = bin(valor1 // valor2)[2:]

    return resposta


def calculadoraMenu():
    while True:
        os.system('cls')
        tabela = Table(title="Calculadora Base 2")
            
        tabela.add_column("Opção", style="cyan", justify="center")
        tabela.add_column("Conversão", style="white")

        tabela.add_row("1", "Adição")
        tabela.add_row("2", "Subtração")
        tabela.add_row("3", "Multiplicação")
        tabela.add_row("4", "Divisão")
        tabela.add_row("0", "Sair")

        console.print(tabela)

        escolha = menu.escolha_menu()

        if escolha == 0:
            return
        
        os.system('cls')
        
        match escolha:
            case 1:
                operador = '+'
            case 2:
                operador = '-'
            case 3:
                operador = 'x'
            case 4:
                operador = '/'
        
        while True:
            try: 
                valor1 = int(input('Digite o primeiro valor: '))
                valor2 = int(input('Digite o segundo valor: '))
                resposta = calculadoraBinaria(valor1, valor2, operador)
                break

            except conv.NumeroInvalidoError as e:
                print(f'Erro: {e}')
            except ValueError as e:
                print(f'Erro: {e}')
            except Exception as e:
                print(f'Erro: {e}')
        
        

        largura = max(len(str(valor1)), len(str(valor2)), len(str(resposta))) + 2

        if operador != '/':
            print(f'{valor1:>{largura}}') if valor1 > valor2 else print(f'{valor2:>{largura}}')
            print(f'{operador}{valor2:>{largura - 1}}') if valor1 > valor2 else print(f'{operador}{valor1:>{largura - 1}}')
            print('—' * largura)
            print(f'{resposta:>{largura}}')


        else:
            print(f'{valor1} |{valor2}')
            print(f'{'':{len(str(valor1))}}{resposta:>{len(str(resposta)) + 2}}')

        sleep(1)
        print()
        input('Pressione enter para continuar')
