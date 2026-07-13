"""Ferramenta para consulta de registros DNS."""

import socket
from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def dns_lookup() -> None:
    """Realiza consultas DNS básicas para um domínio."""
    clear_screen()
    print_header("Consulta DNS")

    try:
        domain = input(f"{Fore.CYAN}Digite o domínio: {Style.RESET_ALL}").strip()
        if not domain:
            show_error("Domínio inválido.")
            pause()
            return

        show_loading(f"Consultando DNS para {domain}...")
        records = {
            "A": socket.gethostbyname_ex(domain)[2],
            "AAAA": [],
            "MX": [],
            "TXT": [],
            "NS": [],
            "CNAME": [],
        }

        show_success("Consulta DNS concluída!")
        print(f"\n{Fore.CYAN}A:{Style.RESET_ALL} {records['A']}")
        print(f"{Fore.CYAN}AAAA:{Style.RESET_ALL} {records['AAAA']}")
        print(f"{Fore.CYAN}MX:{Style.RESET_ALL} {records['MX']}")
        print(f"{Fore.CYAN}TXT:{Style.RESET_ALL} {records['TXT']}")
        print(f"{Fore.CYAN}NS:{Style.RESET_ALL} {records['NS']}")
        print(f"{Fore.CYAN}CNAME:{Style.RESET_ALL} {records['CNAME']}")
    except socket.gaierror as exc:
        show_error(f"Não foi possível resolver o domínio: {exc}")
    except Exception as exc:
        show_error(f"Erro ao consultar DNS: {exc}")

    pause()
