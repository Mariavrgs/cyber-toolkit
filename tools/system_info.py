"""Ferramenta para exibir informações do sistema."""

import os
import platform
import shutil
import socket

from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_success


def show_system_info() -> None:
    """Exibe dados básicos do sistema operacional e hardware."""
    clear_screen()
    print_header("Informações do Sistema")

    try:
        cpu_count = os.cpu_count() or "N/A"
        disk_path = os.path.abspath(os.sep)
        ram = shutil.disk_usage(disk_path)
        try:
            mem = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
            mem_gb = mem // (1024**3)
        except (AttributeError, ValueError, OSError):
            mem_gb = "N/A"

        show_success("Informações coletadas com sucesso!")
        print(f"\n{Fore.CYAN}Sistema operacional:{Style.RESET_ALL} {platform.system()} {platform.release()}")
        print(f"{Fore.CYAN}Versão:{Style.RESET_ALL} {platform.version()}")
        print(f"{Fore.CYAN}CPU:{Style.RESET_ALL} {platform.processor() or 'N/A'}")
        print(f"{Fore.CYAN}Núcleos:{Style.RESET_ALL} {cpu_count}")
        print(f"{Fore.CYAN}RAM:{Style.RESET_ALL} {mem_gb} GB")
        print(f"{Fore.CYAN}Disco:{Style.RESET_ALL} {ram.total // (1024**3)} GB total")
    except Exception as exc:
        show_error(f"Não foi possível obter informações do sistema: {exc}")

    pause()
