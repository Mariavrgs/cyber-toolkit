"""Ferramenta para geração de senhas fortes."""

import secrets
import string
from typing import List

from colorama import Fore, Style

try:
    import pyperclip
except ImportError:  # pragma: no cover - fallback simples
    pyperclip = None

from core.utils import clear_screen, pause, print_header, show_error, show_loading, show_success


def generate_password() -> None:
    """Gera uma senha forte baseada nas opções do usuário."""
    clear_screen()
    print_header("Gerador de Senhas Fortes")

    try:
        length = int(input(f"{Fore.CYAN}Tamanho da senha: {Style.RESET_ALL}"))
        if length <= 0:
            show_error("O tamanho deve ser maior que zero.")
            pause()
            return

        use_symbols = input("Incluir símbolos? (s/n): ").strip().lower() == "s"
        use_numbers = input("Incluir números? (s/n): ").strip().lower() == "s"

        characters = string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = "".join(secrets.choice(characters) for _ in range(length))
        show_loading("Gerando senha...")
        show_success("Senha gerada com sucesso!")
        print(f"\n{Fore.MAGENTA}Senha: {Style.RESET_ALL}{password}")

        copy_choice = input("Copiar para a área de transferência? (s/n): ").strip().lower()
        if copy_choice == "s":
            if pyperclip is None:
                show_error("A biblioteca pyperclip não está disponível. A senha foi exibida na tela.")
            else:
                pyperclip.copy(password)
                show_success("Senha copiada para a área de transferência.")
    except ValueError:
        show_error("Digite um valor numérico válido para o tamanho.")
    except Exception as exc:
        show_error(f"Não foi possível gerar a senha: {exc}")

    pause()
