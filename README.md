# ReconhecedorDeAlvo

Projeto de um scanner de reconhecimento de alvo em Python que integra múltiplas ferramentas para coleta de informações em testes de invasão.

## Introdução

Este utilitário CLI reúne várias ferramentas de reconhecimento, facilitando a análise inicial de alvos web em um só lugar. O objetivo é apoiar práticas de análise e segurança ofensiva, como parte do processo de footprinting em testes de invasão, utilizando técnicas de coleta passiva e ativa.

## Requisitos do Sistema

- Python 3.10 ou superior
- Sistema operacional com suporte a terminal (Linux, macOS ou Windows com CMD/Powershell)

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências executando na pasta do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

Execute o arquivo `main.py`. Um menu interativo será exibido no terminal. Basta selecionar o número correspondente à ferramenta desejada e seguir as instruções.

## Ferramentas Disponíveis

- **WHOIS Lookup**: Recupera informações públicas do registro de domínios, como dados do titular, datas e servidores.
- **Enumeração de Subdomínios**: Técnica de brute-force usando dicionários para descobrir subdomínios válidos.
- **DNS Enumerator**: Varredura por registros DNS (A, AAAA, MX, SOA, TXT etc.), útil para mapear a infraestrutura do alvo.
- **WAF Identifier**: Detecta se há Web Application Firewall ativo, baseado em respostas alteradas por payloads suspeitos.
- **Port Scanner**: Scanner simples de portas TCP, para verificar quais serviços estão disponíveis em um host.  
  O portscanner foi desenvolvido no Roteiro 1. Para mais informações, acesse: [https://github.com/HenriqueFBadin/TecHackPortScanner.git](https://github.com/HenriqueFBadin/TecHackPortScanner.git)

## Entradas e Saídas

A maioria das ferramentas pedirá uma URL ou domínio como entrada. Os resultados são impressos diretamente no terminal.

## Estrutura Modular

Cada ferramenta é implementada em um script separado, podendo ser usada de forma autônoma ou integrada pelo menu principal (`main.py`).

## Linguagens e Bibliotecas

- **Python 3**
- **Bibliotecas utilizadas:**
  - `socket`: varredura de portas
  - `dns.resolver` (dnspython): consulta de registros DNS
  - `whois`: acesso a informações de registro de domínios
  - `wafw00f`: identificação de WAFs por fingerprint

## Referências

### Whois

- https://registro.br/tecnologia/ferramentas/whois
- https://youtu.be/4u5BRgZRoAs?si=FnVG8xEGtVkwAdKi

### Subdomain

- https://youtu.be/E5BklV9I2-4?si=NWXWvycRhnysHHQp
- https://github.com/rbsec/dnscan

### DNS Enumerator

- https://youtu.be/SLQrbjeVrk0?si=OpIskzaghPIIh8g6
- https://medium.com/@jsquared7/dns-enumeration-using-python-772bbeea7b0e

### WAF Identifier

- https://github.com/EnableSecurity/wafw00f

### Port Scanner

- https://github.com/HenriqueFBadin/TecHackPortScanner.git
