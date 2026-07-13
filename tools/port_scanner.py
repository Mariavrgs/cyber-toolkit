"""Ferramenta para escanear portas em um host."""

import socket
from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def scan_ports() -> None:
    """Varre um intervalo de portas em um host."""
    clear_screen()
    print_header("Scanner de Portas")

    try:
        host = input(f"{Fore.CYAN}Digite o host ou IP: {Style.RESET_ALL}").strip()
        start_port = int(input(f"{Fore.CYAN}Porta inicial: {Style.RESET_ALL}"))
        end_port = int(input(f"{Fore.CYAN}Porta final: {Style.RESET_ALL}"))

        if start_port > end_port:
            show_error("A porta inicial não pode ser maior que a final.")
            pause()
            return

        show_loading(f"Escaneando portas em {host}...")
        open_ports = []
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)

        if open_ports:
            show_success("Portas abertas encontradas!")
            print(f"\n{Fore.CYAN}Portas abertas:{Style.RESET_ALL} {open_ports}")
        else:
            show_error("Nenhuma porta aberta encontrada.")
    except ValueError:
        show_error("Digite valores numéricos válidos para as portas.")
    except socket.gaierror as exc:
        show_error(f"Host inválido: {exc}")
    except Exception as exc:
        show_error(f"Erro ao escanear portas: {exc}")

    pause()
