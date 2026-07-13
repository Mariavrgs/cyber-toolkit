"""Gerenciamento do menu principal e navegação da aplicação."""

import sys
from colorama import Fore, Style, init

from core.banner import get_banner
from core.utils import clear_screen, pause, print_header, show_error, show_success
from tools.password import generate_password
from tools.hash import generate_sha256
from tools.ip import discover_public_ip
from tools.ping import ping_host
from tools.website import check_website
from tools.dns import dns_lookup
from tools.whois_lookup import whois_lookup
from tools.port_scanner import scan_ports
from tools.geoip import geoip_lookup
from tools.system_info import show_system_info
from tools.file_hash import verify_file_integrity

init(autoreset=True)


def show_menu() -> None:
    """Exibe o menu principal da aplicação."""
    clear_screen()
    print(get_banner())
    print(f"{Fore.YELLOW}Menu principal{Style.RESET_ALL}")
    print()
    print("[1] Gerador de Senhas Fortes")
    print("[2] Gerador de Hash SHA256")
    print("[3] Descobrir IP Público")
    print("[4] Ping em um Host")
    print("[5] Verificar se um Site está Online")
    print("[6] Informações DNS")
    print("[7] Consulta WHOIS")
    print("[8] Scanner de Portas")
    print("[9] Geolocalização de IP")
    print("[10] Informações do Sistema")
    print("[11] Verificar Integridade de Arquivos")
    print("[0] Sair")
    print()


def run() -> None:
    """Loop principal da aplicação."""
    while True:
        show_menu()
        choice = input(f"{Fore.CYAN}Escolha uma opção: {Style.RESET_ALL}").strip()

        try:
            if choice == "1":
                generate_password()
            elif choice == "2":
                generate_sha256()
            elif choice == "3":
                discover_public_ip()
            elif choice == "4":
                ping_host()
            elif choice == "5":
                check_website()
            elif choice == "6":
                dns_lookup()
            elif choice == "7":
                whois_lookup()
            elif choice == "8":
                scan_ports()
            elif choice == "9":
                geoip_lookup()
            elif choice == "10":
                show_system_info()
            elif choice == "11":
                verify_file_integrity()
            elif choice == "0":
                show_success("Encerrando o Cyber Toolkit...")
                sys.exit(0)
            else:
                show_error("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            show_error("Operação cancelada pelo usuário.")
        except Exception as exc:
            show_error(f"Ocorreu um erro inesperado: {exc}")

        pause()
