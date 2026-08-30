# Criado por Gabriel Lopes Videira

import funcoes.menus as menu
from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()

while True:
    console.clear()
    menu.mostrar_menu()

    escolha = menu.escolha_menu()

    console.clear()
    match escolha:
        case 1:
            menu.conversor_menu()
        case 2:
            menu.operacoes_menu()
        case 0:
            print("Volte sempre!")
            sleep(2)
            break