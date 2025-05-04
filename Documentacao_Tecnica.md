# Documentação Técnica - Ferramentas de Reconhecimento

## 1. Visão Geral

Este projeto é um conjunto de ferramentas de reconhecimento de alvos web, voltadas para práticas de análise e segurança ofensiva, como parte de um processo de footprinting em testes de invasão. São utilizadas técnicas de coleta passiva e ativa.

## 2. Tecnologias e Conceitos Aplicados

- **WHOIS Lookup**: Recupera informações públicas do registro de domínios, como dados do titular, datas e servidores.
- **Enumeração de Subdomínios**: Técnica de brute-force usando dicionários para descobrir subdomínios válidos.
- **DNS Enumerator**: Varredura por registros DNS (A, AAAA, MX, SOA, TXT etc.), útil para mapear a infraestrutura do alvo.
- **WAF Identifier**: Detecta se há Web Application Firewall ativo, baseado em respostas alteradas por payloads suspeitos.
- **Port Scanner**: Scanner simples de portas TCP, para verificar quais serviços estão disponíveis em um host.  
  O portscanner foi desenvolvido no Roteiro 1. Para mais informações, acesse: [https://github.com/HenriqueFBadin/TecHackPortScanner.git](https://github.com/HenriqueFBadin/TecHackPortScanner.git)

## 3. Estrutura Modular

Cada ferramenta é implementada em um script separado, podendo ser usada de forma autônoma ou integrada pelo menu principal.

## 4. Linguagens e Bibliotecas

A linguagem utilizada é Python. Foram utilizadas bibliotecas como:

- socket: varredura de portas
- dns.resolver (dnspython): consulta de registros DNS
- whois: acesso a informações de registro de domínios
- wafw00f: identificação de WAFs por fingerprint

## 5. Referências

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
