"""Ferramenta para realizar ping em um host."""

import subprocess
import platform

from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def ping_host() -> None:
    """Executa um ping simples em um host informado."""
    clear_screen()
    print_header("Ping em um Host")

    try:
        host = input(f"{Fore.CYAN}Digite o host ou IP: {Style.RESET_ALL}").strip()
        if not host:
            show_error("Host inválido.")
            pause()
            return

        show_loading(f"Enviando pacotes para {host}...")
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "4", host]
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)

        if result.returncode == 0:
            show_success("Ping concluído com sucesso!")
            print(result.stdout)
        else:
            show_error("Não foi possível completar o ping.")
            print(result.stderr)
    except FileNotFoundError:
        show_error("O comando ping não está disponível neste ambiente.")
    except subprocess.TimeoutExpired:
        show_error("A operação de ping excedeu o tempo limite.")
    except Exception as exc:
        show_error(f"Erro ao executar o ping: {exc}")

    pause()
