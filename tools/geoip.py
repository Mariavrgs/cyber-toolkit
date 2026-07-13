"""Ferramenta para geolocalização de IP."""

import requests
from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def geoip_lookup() -> None:
    """Consulta um IP e exibe dados geográficos."""
    clear_screen()
    print_header("Geolocalização de IP")

    try:
        ip_address = input(f"{Fore.CYAN}Digite o IP: {Style.RESET_ALL}").strip()
        if not ip_address:
            show_error("IP inválido.")
            pause()
            return

        show_loading(f"Consultando geolocalização para {ip_address}...")
        response = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=10)
        response.raise_for_status()
        data = response.json()

        show_success("Geolocalização obtida com sucesso!")
        print(f"\n{Fore.CYAN}Cidade:{Style.RESET_ALL} {data.get('city', 'N/A')}")
        print(f"{Fore.CYAN}Estado:{Style.RESET_ALL} {data.get('region', 'N/A')}")
        print(f"{Fore.CYAN}País:{Style.RESET_ALL} {data.get('country', 'N/A')}")
        print(f"{Fore.CYAN}Latitude:{Style.RESET_ALL} {data.get('loc', 'N/A')}")
        print(f"{Fore.CYAN}Provedor:{Style.RESET_ALL} {data.get('org', 'N/A')}")
    except requests.RequestException as exc:
        show_error(f"Falha na consulta de geolocalização: {exc}")
    except Exception as exc:
        show_error(f"Erro inesperado: {exc}")

    pause()
