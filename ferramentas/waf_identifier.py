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
        f"\n===================== Buscando o WAF de {target_domain} ====================="
    )

    waf_detector = WAFW00F(target=target_domain)

    waf_detected = waf_detector.identwaf()

    if waf_detector.knowledge.get("wafname"):
        if type(waf_detector.knowledge["wafname"]) == list:
            for waf in waf_detector.knowledge["wafname"]:
                print(f"\nWAF detectado: {waf}")
        else:
            print(f"\nWAF detectado: {waf_detector.knowledge['wafname']}")

    else:
        print("\nA identificação do WAF falhou")
        print("\nNenhum WAF detectado.")
