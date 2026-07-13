"""Utilitários compartilhados para a aplicação."""

import os
import sys
import time
from typing import Optional

from colorama import Fore, Style


def clear_screen() -> None:
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title: str) -> None:
    """Exibe um cabeçalho padrão para as telas."""
    print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{title}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")


def show_loading(message: str = "Processando...") -> None:
    """Exibe uma mensagem de processamento simples."""
    print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")


def show_success(message: str) -> None:
    """Exibe uma mensagem de sucesso."""
    print(f"{Fore.GREEN}[✓] {message}{Style.RESET_ALL}")


def show_error(message: str) -> None:
    """Exibe uma mensagem de erro amigável."""
    print(f"{Fore.RED}[!] {message}{Style.RESET_ALL}")


def pause() -> None:
    """Pausa a execução até o usuário pressionar Enter."""
    input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")


def safe_input(prompt: str, default: Optional[str] = None) -> str:
    """Lê entrada do usuário com valor padrão opcional."""
    value = input(prompt).strip()
    if not value and default is not None:
        return default
    return value
