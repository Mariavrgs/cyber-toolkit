"""Ferramenta para verificar integridade de arquivos."""

import hashlib
from pathlib import Path

from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def verify_file_integrity() -> None:
    """Calcula hashes MD5, SHA1 e SHA256 de um arquivo."""
    clear_screen()
    print_header("Verificar Integridade de Arquivos")

    try:
        file_path = input(f"{Fore.CYAN}Digite o caminho do arquivo: {Style.RESET_ALL}").strip()
        if not file_path:
            show_error("Caminho inválido.")
            pause()
            return

        path = Path(file_path)
        if not path.exists():
            show_error("Arquivo não encontrado.")
            pause()
            return

        show_loading("Calculando hashes...")
        hashes = {
            "MD5": hashlib.md5(),
            "SHA1": hashlib.sha1(),
            "SHA256": hashlib.sha256(),
        }
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                for digest in hashes.values():
                    digest.update(chunk)

        show_success("Hashes calculados com sucesso!")
        print(f"\n{Fore.CYAN}MD5:{Style.RESET_ALL} {hashes['MD5'].hexdigest()}")
        print(f"{Fore.CYAN}SHA1:{Style.RESET_ALL} {hashes['SHA1'].hexdigest()}")
        print(f"{Fore.CYAN}SHA256:{Style.RESET_ALL} {hashes['SHA256'].hexdigest()}")
    except Exception as exc:
        show_error(f"Erro ao calcular hashes: {exc}")

    pause()
