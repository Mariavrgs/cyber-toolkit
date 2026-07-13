"""Funções para exibir o banner principal do Cyber Toolkit."""

from colorama import Fore, Style


def get_banner() -> str:
    """Retorna o banner ASCII estilizado para a aplicação."""
    return f"""
{Fore.CYAN}================================================={Style.RESET_ALL}
{Fore.MAGENTA}                 CYBER TOOLKIT{Style.RESET_ALL}
{Fore.CYAN}================================================={Style.RESET_ALL}
"""
