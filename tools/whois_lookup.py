"""Ferramenta para consulta WHOIS simplificada."""

import subprocess
import platform

from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def whois_lookup() -> None:
    """Executa uma consulta WHOIS para um domínio."""
    clear_screen()
    print_header("Consulta WHOIS")

    try:
        domain = input(f"{Fore.CYAN}Digite o domínio: {Style.RESET_ALL}").strip()
        if not domain:
            show_error("Domínio inválido.")
            pause()
            return

        show_loading(f"Consultando WHOIS para {domain}...")
        command = ["whois", domain]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        if result.returncode == 0:
            show_success("Consulta WHOIS concluída!")
            print(result.stdout)
        else:
            show_error("Não foi possível obter informações WHOIS.")
            print(result.stderr)
    except FileNotFoundError:
        show_error("O utilitário WHOIS não está instalado.")
    except subprocess.TimeoutExpired:
        show_error("A consulta WHOIS excedeu o tempo limite.")
    except Exception as exc:
        show_error(f"Erro ao consultar WHOIS: {exc}")

    pause()
