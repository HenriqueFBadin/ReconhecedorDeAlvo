import dns.resolver
import os


def limpar_dominio_por_subdominios(entrada, subdomain_list):
    partes = entrada.split(".")
    for i, parte in enumerate(partes):
        if parte.lower() not in subdomain_list:
            return ".".join(partes[i:])
    return ".".join(partes)


def subdom_scanner():
    domain = input(
        "Informe qual o domínio que deseja analizar os subdomínios disponíveis: "
    )

    print("Quantos subdomínios deseja analisar?")
    print("Lista curta de subdomínios: 100 subdominios")
    print("Lista média: 1.000 subdominios")
    print("Lista completa: 10.000 subdominios")

    opcoes_validas = ["100", "1000", "10000"]
    n_subdomains = input("Digite 100, 1000 ou 10000: ")

    while n_subdomains not in opcoes_validas:
        print("Valor inválido. Por favor, digite 100, 1000 ou 10000.")
        n_subdomains = input("Digite novamente: ")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    subdomain_file_path = os.path.join(current_dir, f"subdomains-{n_subdomains}.txt")

    with open(subdomain_file_path, "r") as file:

        all_domains = file.read()
        subdomains_list = all_domains.splitlines()

    domain = limpar_dominio_por_subdominios(domain, subdomains_list)
    print(
        f"\n======================== Domínio sendo analisado: {domain} ========================"
    )

    subdomain_store = []
    total = len(subdomains_list)
    progresso_mostrado = {10: False, 25: False, 50: False, 75: False, 99: False}

    for i, subdom in enumerate(subdomains_list, start=1):
        try:
            ip_value = dns.resolver.resolve(f"{subdom}.{domain}")
            if ip_value:
                subdomain = f"{subdom}.{domain}"
                if subdomain not in subdomain_store:
                    subdomain_store.append(subdomain)
                    print(f"{subdomain} válido")

        except (
            dns.resolver.NoAnswer,
            dns.resolver.NoNameservers,
            dns.resolver.NXDOMAIN,
        ):
            progresso = float((i / total) * 100)

            for ponto in [10, 25, 50, 75, 99]:
                if progresso >= ponto and not progresso_mostrado[ponto]:
                    print(f"\n==============Progresso: {ponto}%==============")
                    progresso_mostrado[ponto] = True
                    break

            continue
        except KeyboardInterrupt:
            quit()

        progresso = float((i / total) * 100)
        for ponto in [10, 25, 50, 75, 99]:
            if progresso >= ponto and not progresso_mostrado[ponto]:
                print(f"\n==============Progresso: {ponto}%==============")
                progresso_mostrado[ponto] = True
                break
