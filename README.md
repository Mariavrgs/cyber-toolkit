# Cyber Toolkit

Cyber Toolkit é um terminal interativo em Python voltado para estudantes de redes e cibersegurança. A aplicação oferece ferramentas úteis para análise, diagnóstico e segurança, com uma interface amigável, colorida e organizada.

## Objetivos

- Oferecer uma coleção de ferramentas úteis para estudantes e profissionais iniciantes.
- Demonstrar boas práticas de arquitetura em Python para projetos de portfólio.
- Criar uma base escalável para futuras funcionalidades de rede, análise e segurança.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd cyber-toolkit
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Dependências

- colorama
- requests
- pyperclip

## Como executar

```bash
python main.py
```

## Estrutura do projeto

```text
cyber-toolkit/
├── main.py
├── requirements.txt
├── README.md
├── core/
│   ├── menu.py
│   ├── banner.py
│   ├── utils.py
├── tools/
│   ├── password.py
│   ├── hash.py
│   ├── ip.py
│   ├── ping.py
│   ├── website.py
│   ├── dns.py
│   ├── whois_lookup.py
│   ├── port_scanner.py
│   ├── geoip.py
│   ├── system_info.py
│   ├── file_hash.py
└── assets/
```

## Funcionalidades

- Gerador de senhas fortes
- Geração de hash SHA256
- Descoberta de IP público
- Ping em hosts
- Verificação de disponibilidade de sites
- Consultas DNS
- Consulta WHOIS
- Scanner de portas
- Geolocalização de IP
- Informações do sistema
- Verificação de integridade de arquivos

## Tecnologias utilizadas

- Python 3
- Colorama
- Requests
- Socket
- hashlib
- subprocess

## Screenshots

- Em breve: capturas de tela da interface interativa.

## Roadmap

- Adicionar scanner de vulnerabilidades
- Implementar monitor de rede
- Criar módulo de captura de pacotes
- Expandir para ferramentas de Blue Team e Red Team

## Licença

Este projeto é distribuído sob a licença MIT.
