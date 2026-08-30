import funcoes.conversor as conv
import funcoes.operacoes_binarias as op
from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()

def escolha_menu(texto = "Escolha uma opção: "):
    while True:
            try:
                escolha = int(input(texto))
                break
    
            except ValueError as e:
                print(f'Erro: {e}')
                sleep(1.5)
    return escolha

def mostrar_menu():
    tabela = Table(title="Bases Númericas")

    tabela.add_column("Opção", style="cyan", justify="center")
    tabela.add_column("Conversão", style="white")

    tabela.add_row("1", "Conversão de bases")
    tabela.add_row("2", "Operações com base 2")
    tabela.add_row("0", "Sair")

    console.print(tabela)

def conversor_menu():
    while True:
        console.clear()
        tabela = Table(title="Conversão de Bases")

        tabela.add_column("Opção", style="cyan", justify="center")
        tabela.add_column("Conversão", style="white")

        tabela.add_row("1", "Conversor Universal")
        tabela.add_row("2", "Praticar conversões")
        tabela.add_row("3", "Como converter cada base")
        tabela.add_row("0", "Voltar")

        console.print(tabela)

        escolha = escolha_menu()

        console.clear()
        match escolha:
            case 1:
                conv.gerenciadorConversoes()
            case 2:
                conv.geradorBases()
            case 3:
                conv.tutorialConversao()
            case 0:
                return

def operacoes_menu():
    while True:
        console.clear()
        tabela = Table(title="Conversão de Bases")

        tabela.add_column("Opção", style="cyan", justify="center")
        tabela.add_column("Conversão", style="white")

        tabela.add_row("1", "Calculadora de base 2")
        tabela.add_row("2", "Praticar operações")
        tabela.add_row("3", "Como calcular as operações")
        tabela.add_row("0", "Voltar")

        console.print(tabela)

        escolha = escolha_menu()

        console.clear()
        match escolha:
            case 1:
                op.calculadoraMenu()
            case 2:
                op.geradorOperacoes()
            case 3:
                op.tutorialOperacoes()
            case  0:
                return
                    