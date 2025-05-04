from ferramentas.dns_enumerator import dns_enum
from ferramentas.subdomain_scanner import subdom_scanner
from ferramentas.waf_identifier import waf_identifier
from ferramentas.whois_lookup import whois_lookup
from ferramentas.portscanner import portscanner

while True:
    print("\n===== MENU DE FERRAMENTAS =====")
    print("[1] WHOIS")
    print("[2] Enumeração de Subdomínios")
    print("[3] Enumeração de DNS")
    print("[4] Verificação de WAF")
    print("[5] Portscanner")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            whois_lookup()
        elif opcao == "2":
            subdom_scanner()
        elif opcao == "3":
            dns_enum()
        elif opcao == "4":
            waf_identifier()
        elif opcao == "5":
            portscanner()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"\n[!] Ocorreu um erro inesperado ao executar a ferramenta: {e}")
        print("[!] Retornando ao menu...")
