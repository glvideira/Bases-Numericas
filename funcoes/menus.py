import funcoes.conversor as conv
from rich.console import Console
from rich.table import Table
from time import sleep

def escolha_menu(texto = "Escolha uma opção: "):
    while True:
            try:
                escolha = int(input(texto))
                break
    
            except ValueError as e:
                print(f'Erro: {e}')
                sleep(1.5)
    return escolha

console = Console()

def conversor_menu():
    while True:
        console.clear()
        tabela = Table(title="Conversor de Bases")

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
                conv.tutorial()
                    