# Manual do Usuário - Ferramentas de Reconhecimento

## 1. Introdução

Este utilitário CLI reúne várias ferramentas de reconhecimento. O objetivo é facilitar a análise inicial de alvos web em um só lugar.

## 2. Requisitos do Sistema

- Python 3.10 ou superior
- Sistema operacional com suporte a terminal

## 3. Instalação das Dependências

Rode o seguinte comando na pasta do projeto para instalar as dependências necessárias:

```
pip install -r requirements.txt
```

Caso queira instalar as dependências manualmente, utilize os seguintes comandos:

```
pip install dnspython
pip install python-whois
pip install wafw00f
```

## 4. Ferramentas Utilizadas

- dnspython
- python-whois
- wafw00f
- socket (nativa do Python)

## 5. Como usar

Execute main.py. Um menu interativo será exibido. Selecione o número correspondente à ferramenta desejada.

## 6. Entradas e Saídas

A maioria das ferramentas pedirá uma URL ou domínio. Os resultados são impressos diretamente no terminal e logo depois o usuário retornará para o menu, permitindo-o fazer mais verificações.

## 7. Referências

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
