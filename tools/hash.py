"""Ferramenta para gerar hashes SHA256."""

import hashlib
from pathlib import Path

from colorama import Fore, Style

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def generate_sha256() -> None:
    """Recebe um texto e gera o hash SHA256."""
    clear_screen()
    print_header("Gerador de Hash SHA256")

    try:
        text = input(f"{Fore.CYAN}Digite o texto: {Style.RESET_ALL}")
        show_loading("Calculando hash...")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        show_success("Hash SHA256 gerado com sucesso!")
        print(f"\n{Fore.MAGENTA}SHA256: {Style.RESET_ALL}{digest}")

        save_choice = input("Salvar em arquivo? (s/n): ").strip().lower()
        if save_choice == "s":
            file_path = Path("hash_output.txt")
            file_path.write_text(digest, encoding="utf-8")
            show_success(f"Hash salvo em {file_path}")
    except Exception as exc:
        show_error(f"Não foi possível gerar o hash: {exc}")

    pause()
