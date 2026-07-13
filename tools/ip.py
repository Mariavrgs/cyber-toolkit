"""Ferramenta para descobrir o IP público e dados básicos de geolocalização."""

import requests
from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def discover_public_ip() -> None:
    """Consulta a API ipinfo.io para obter dados do IP público."""
    clear_screen()
    print_header("Descobrir IP Público")

    try:
        show_loading("Consultando serviço externo...")
        response = requests.get("https://ipinfo.io/json", timeout=10)
        response.raise_for_status()
        data = response.json()

        show_success("Dados obtidos com sucesso!")
        print(f"\n{Fore.CYAN}IP:{Style.RESET_ALL} {data.get('ip', 'N/A')}")
        print(f"{Fore.CYAN}Cidade:{Style.RESET_ALL} {data.get('city', 'N/A')}")
        print(f"{Fore.CYAN}País:{Style.RESET_ALL} {data.get('country', 'N/A')}")
        print(f"{Fore.CYAN}ISP:{Style.RESET_ALL} {data.get('org', 'N/A')}")
    except requests.RequestException as exc:
        show_error(f"Falha na requisição: {exc}")
    except ValueError as exc:
        show_error(f"Resposta inválida do servidor: {exc}")
    except Exception as exc:
        show_error(f"Não foi possível consultar o IP: {exc}")

    pause()
