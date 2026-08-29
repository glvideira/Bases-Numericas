# Criado por Gabriel Lopes Videira

import funcoes.menus as menu
from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()



def mostrar_menu():
    tabela = Table(title="Bases Númericas")

    tabela.add_column("Opção", style="cyan", justify="center")
    tabela.add_column("Conversão", style="white")

    tabela.add_row("1", "Conversão de bases")
    tabela.add_row("2", "Operações aritméticas com base 2")
    tabela.add_row("0", "Sair")

    console.print(tabela)

while True:
    console.clear()
    mostrar_menu()

    escolha = menu.escolha_menu()

    match escolha:
        case 1:
            menu.conversor_menu()






