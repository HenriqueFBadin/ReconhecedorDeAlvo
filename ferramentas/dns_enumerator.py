import dns.resolver


def dns_enum():
    target_domain = input("Insira o domínio que quer analisar: ")
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["8.8.8.8", "1.1.1.1"]

    print(f"\nConsultando registros DNS de {target_domain}")

    for record_type in record_types:
        try:
            answers = resolver.resolve(target_domain, record_type)
        except (
            dns.resolver.NoAnswer,
            dns.resolver.NoNameservers,
            dns.resolver.NXDOMAIN,
        ):
            continue

        print(f"\n{record_type} records for {target_domain}:")
        for record_data in answers:
            print(f" {record_data}")
