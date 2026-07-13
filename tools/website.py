"""Ferramenta para verificar se um site está online."""

import requests
from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def check_website() -> None:
    """Consulta um site e exibe informações HTTP de resposta."""
    clear_screen()
    print_header("Verificador de Sites")

    try:
        url = input(f"{Fore.CYAN}Digite a URL do site (ex.: https://example.com): {Style.RESET_ALL}").strip()
        if not url:
            show_error("URL inválida.")
            pause()
            return

        show_loading(f"Consultando {url}...")
        response = requests.get(url, timeout=10)
        show_success("Consulta concluída com sucesso!")
        print(f"\n{Fore.CYAN}Status HTTP:{Style.RESET_ALL} {response.status_code}")
        print(f"{Fore.CYAN}Tempo de resposta:{Style.RESET_ALL} {response.elapsed.total_seconds():.2f}s")
        print(f"{Fore.CYAN}Tamanho da página:{Style.RESET_ALL} {len(response.content)} bytes")
        print(f"{Fore.CYAN}Server:{Style.RESET_ALL} {response.headers.get('server', 'N/A')}")
        print(f"{Fore.CYAN}Content-Type:{Style.RESET_ALL} {response.headers.get('content-type', 'N/A')}")
    except requests.RequestException as exc:
        show_error(f"Falha ao acessar o site: {exc}")
    except Exception as exc:
        show_error(f"Erro inesperado: {exc}")

    pause()
