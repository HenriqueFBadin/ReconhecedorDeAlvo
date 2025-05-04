from wafw00f.main import WAFW00F


def waf_identifier():
    while True:
        target_domain = input(
            "Insira uma URL para detecção do WAF (com http:// ou https://): "
        ).strip()
        if target_domain.startswith("http://") or target_domain.startswith("https://"):
            break
        else:
            print("Por favor, inclua 'http://' ou 'https://' no início da URL.")

    print(
        f"\n===================== Buscando o WAF de {target_domain} =====================\n"
    )

    waf_detector = WAFW00F(target=target_domain)

    if waf_detector.knowledge.get("wafname"):
        print(f"\nWAF detected: {waf_detector.knowledge['wafname']}")
    else:
        print("\nA identificação do WAF falhou, tentando uma identificação genérica\n")
        waf_detector.genericdetect()
        print("\nNenhum WAF detectado.")
